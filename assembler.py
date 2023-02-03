import sys

lookup = {
    "mova": "00000001",
    "movb": "00000010",
    "add":  "00000011",
    "sub":  "00000100",
    "sto":  "00000101",
    "ldd":  "00000110",
    "jmp":  "00000111",
}

def assemble(filename):
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

    instructions = []
    for line in lines:
        payload = line.split(" ")
        opcode = payload[0]
        try:
            operand = payload[1]
        except IndexError:
            operand = "00000000"
        ins = lookup.get(opcode) + bin(int(operand)).replace("0b", "").zfill(16)
        instructions.append(ins)

    with open("output.hex", "w") as f:
        f.write("v2.0 raw")
        f.write("\r")
        for hexed in instructions:
            print(hexed)
            f.write(hex(int(hexed, 2)) + " ")
        f.write("\r")

if __name__ == "__main__":
    filename = sys.argv[1]  
    assemble(filename)