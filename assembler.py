import sys
import itertools

virtual_stack_pointer = 3000
char_offset = -2
count = 0
string_pointer = 1000

opcodes = {
    "mova": "00000001",
    "movb": "00000010",
    "ldia": "00000011",
    "ldib": "00000100",
    "add" : "00000101",
    "sub" : "00000110",
    "jmp" : "00000111",
    "jnz" : "00001000",
    "lda" : "00001001",
    "ldb" : "00001010",
    "outb": "00001011",
}

def write_hex(hex_data):
    with open("output.hex", "w") as f:
        f.write("v2.0 raw")
        f.write("\r")
        for hexed in hex_data:
            f.write(hexed + " ")
        f.write("\r")

def expand_macro(macros, name, data, index, final_data, macro_end):
    lines_to_remove = []
    offset = 0
    line = data[index + offset]
    #print(f"EXPANDING MACRO: {line}")
    while "}" not in line:
        lines_to_remove.append(index + offset)
        offset += 1
        line = data[index + offset]
        macros[name]["expansion"].append(line)
    macros[name]["expansion"].pop()
    macro_end = index + offset
    return macro_end

def scan_for_macros(data, macro_end):
    final_data = []
    macros = {}
    for index, line in enumerate(data):
        if "$" in line:
            macro_name = line.split('$')[1].split(' ')[0]
            macros[macro_name] = {"args": [], "expansion": []}

            #print(f"FOUND MACRO NAMED: {macro_name}")
            args = line.split(" ")[1:]
            for arg in args:
                if "%" in arg:
                    macros[macro_name]["args"].append(arg)

            macro_end = expand_macro(macros, macro_name, data, index, final_data, macro_end)

    return macros, macro_end

num_chars = 0
lines = 0

def recursivly_assemble_macros(data, macros, virtual_stack_pointer, char_offset):
    global num_chars, lines
    for index, line in enumerate(data):
        opcode = line.split(" ")[0]
        macro = macros.get(opcode, None)
        if macro:
            replace = macro.copy()
            operands = line.split(" ")[1:]
            #data[index] = macro["expansion"]
            data[index] = []
            for i, part in enumerate(macro["expansion"]):
                backup = part
                try:
                    part_args = part.split(" ")[1]
                except:
                    part_args = []

                if "!!%OFFSET++" in part:
                    num_chars += 1
                    if num_chars % 6 == 0:
                        char_offset += 167
                        #num_chars = 0
                    else:
                        char_offset += 5

                if part_args == []:
                    if part == "!!%RSP++":
                        virtual_stack_pointer += 1
                    elif part == "!!%RSP--":
                        virtual_stack_pointer -= 1
                else:
                    if part_args == "%RSP":
                        part = part.replace(part_args, str(virtual_stack_pointer))
                    elif "%OFFSET" in part_args:
                        part = part.replace("%OFFSET", str(char_offset))
                    else:
                        if operands:
                            part = part.replace(part_args, str(operands[i]))
                    data[index].append(part)
    return data

def assemble_macros(data, macros, virtual_stack_pointer, char_offset):
    data = recursivly_assemble_macros(data, macros, virtual_stack_pointer, char_offset)
    
    flat_list = []
    for sublist in data:
        if type(sublist) == list:
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    data = flat_list
    return data

def expand_include_dirs(data):
    new_data = []
    for num, line in enumerate(data):
        if "&include" in line: #then we know this is an include
            data_dir = str(line.split(" ")[1]).strip("\"")
            with open(data_dir, "r") as include_file:
                for include_line in include_file.readlines():
                    include_line = include_line.replace("\n", "").replace("  ", "")
                    new_data.append(include_line)
    for d in data:
        if d != "":
            new_data.append(d)
    return new_data

def load_strings(data, string_pointer, strings, string_values):
    for x in range(2):
        append_data = []
        lines_to_remove = []
        for i, line in enumerate(data):
            if "lds" in line:   
                ptr = string_pointer
                str_data = line.split(":\"")[1].split("->")[0]
                str_name = line.split("->")[1]
                strings[str_name] = str_data
                str_data = str_data[0:len(str_data) - 1]

                append_data.append(f"mem {len(str_data)} {string_pointer}")
                string_pointer += 1

                for char in str_data:
                    append_data.append(f"mem {ord(char)} {string_pointer}")
                    string_pointer += 1
                strings[str_name] = ptr
                string_values[ptr] = len(str_data)
                for i in range(len(str_data)):
                    string_values[ptr+i+1] = str_data[i]
                data.remove(line)
                data.append(append_data)
    return data

string_prints = {
    65: "drawchara",
    66: "drawcharb",
    67: "drawcharc",
    68: "drawchard",
    69: "drawchare",
    70: "drawcharf",
    71: "drawcharg",
    72: "drawcharh",
    73: "drawchari",
    74: "drawcharj",
    75: "drawchark",
    76: "drawcharl",
    77: "drawcharm",
    78: "drawcharn",
    79: "drawcharo",
    80: "drawcharp",
    81: "drawcharq",
    82: "drawcharr",
    83: "drawchars",
    84: "drawchart",
    85: "drawcharu",
    86: "drawcharv",
    87: "drawcharw",
    88: "drawcharx",
    89: "drawchary",
    90: "drawcharz",
    32: "drawcharspace",
}

def puts(data, strings, string_values):
    for i, line in enumerate(data):
        if "puts" in line:
            data[i] = []
            pointer_name = line.split(" ")[1]
            pointer = strings[pointer_name]
            length = string_values[pointer]
            for x in range(length):
                data[i].append(string_prints[ord(string_values[pointer+x+1])]) 
    return data

def assemble(filename, virtual_stack_pointer, char_offset, count):
    hex_data = []
    data = []
    labels = {}
    macro_end = 0
    with open(filename , "r") as f:
        for num, line in enumerate(f.readlines()): #Before we can parse we must scan for macros
            ln = line.replace("\n", "").replace("  ", "")
            data.append(ln)
    
    data = expand_include_dirs(data)

    strings = {}
    string_values = {}
    data = load_strings(data, string_pointer, strings, string_values)
    data = puts(data, strings, string_values)
    
    flat_list = []
    for sublist in data:
        if type(sublist) == list:
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    data = flat_list

    macros, macro_end = scan_for_macros(data, macro_end)
    data = data[macro_end+2:]
    data = assemble_macros(data, macros, virtual_stack_pointer, char_offset)
    data = assemble_macros(data, macros, virtual_stack_pointer, char_offset)
    data = assemble_macros(data, macros, virtual_stack_pointer, char_offset)
    data = assemble_macros(data, macros, virtual_stack_pointer, char_offset)
    print(data)
    labels = {}
    for num, line in enumerate(data): #Before we can parse we must scan for macros
        ln = line.replace("\n", "").replace("  ", "")
        if ":" in ln:
            labels[ln.replace(":", "")] = num - 1
            data.remove(line)

    for line in data:
        data = line.split(" ")
        opcode = data[0].replace("\n", "")
        if len(data) > 1:
            operand = data[1].replace("\n", "")
            if "+" in operand:
                potential_str_arg = operand.split("+")[0]
                if potential_str_arg in strings:
                    potential_str_arg = strings[potential_str_arg]
                    
                operand = int(potential_str_arg) + int(operand.split("+")[1])
        else:
            operand = None
        if operand in labels:
            operand = labels[operand]
        operand = strings.get(operand, operand)
        instruction = (opcodes[opcode], (bin(int(operand)).replace("0b", "")).rjust(16, "0") if operand else "0".rjust(16, "0"))
        instruction = str(instruction[0] + instruction[1])
        hexed = format(int(instruction, 2),'x')
        hexed.rjust(4,'0')
        hex_data.append(hexed)

    write_hex(hex_data)

if __name__ == "__main__":
    filename = sys.argv[1]
    assemble(filename, virtual_stack_pointer, char_offset, count)

