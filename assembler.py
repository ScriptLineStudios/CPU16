import sys
import itertools

virtual_stack_pointer = 3000

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
}

macros = {
    "mem" : ["mova @", "ldia @"],
    "push": ["mova @", f"ldia {virtual_stack_pointer}"],
    "pop" : [f"lda {virtual_stack_pointer}"],
}

def write_hex(hex_data):
    with open("output.hex", "w") as f:
        f.write("v2.0 raw")
        f.write("\r")
        for hexed in hex_data:
            f.write(hexed + " ")
        f.write("\r")

def assemble(filename):
    hex_data = []
    data = []
    with open(filename , "r") as f:
        for line in f.readlines(): #Before we can parse we must scan for macros
            data.append(line.replace("\n", ""))

    for index, line in enumerate(data):
        opcode = line.split(" ")[0]
        macro = macros.get(opcode, None)
        if macro:
            operands = line.split(" ")[1:]
            data[index] = [sub.replace("@", operands[i]) for i, sub in enumerate(macro)]
    
    flat_list = []
    for sublist in data:
        if type(sublist) == list:
            for item in sublist:
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    data = flat_list
    print(data)
    for line in data:
        data = line.split(" ")
        opcode = data[0].replace("\n", "")
        if len(data) > 1:
            operand = data[1].replace("\n", "")
        else:
            operand = None
        instruction = (opcodes[opcode], (bin(int(operand)).replace("0b", "")).rjust(16, "0") if operand else "0".rjust(16, "0"))
        instruction = str(instruction[0] + instruction[1])
        hexed = format(int(instruction, 2),'x')
        hexed.rjust(4,'0')
        hex_data.append(hexed)

    write_hex(hex_data)

if __name__ == "__main__":
    filename = sys.argv[1]
    assemble(filename)
