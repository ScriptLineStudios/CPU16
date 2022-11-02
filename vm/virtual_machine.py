import binascii

class VirtualMachine:
    def __init__(self):
        self.program = []
        self.instruction_pointer = 0

        self.RA = 0
        self.RB = 0
        self.RAM = [0] * 10000

        self.instructions = {
            "00000001": 0,
            "00000010": 1,
            "00000011": 2,
            "00000100": 3,
            "00000101": 4,
            "00000110": 5,
            "00000111": 6,
            "00001000": 7,
            "00001001": 8,
            "00001010": 9,
            "00001011": 10, 
        }

        self.instruction_macros = [self.movea, self.moveb, self.ldia, self.ldib, self.add, self.sub, self.jmp, self.jnz, self.lda, self.ldb, self.outb]
        self.io = []

    def attach(self, IODevice):
        self.io.append(IODevice)

    def movea(self, imm):
        self.RA = imm

    def moveb(self, imm):
        self.RB = imm
    
    def ldia(self, addr):
        self.RAM[addr] = self.RA
    
    def ldib(self, addr):
        self.RAM[addr] = self.RB

    def add(self, void):
        self.RA += self.RB

    def sub(self, void):
        self.RA -= self.RB

    def jmp(self, imm):
        self.instruction_pointer = imm

    def jnz(self, imm):
        if self.RA != 0:
            self.instruction_pointer = imm
        
    def lda(self, addr):
        self.RA = self.RAM[addr]

    def ldb(self, addr):
        self.RB = self.RAM[addr]

    def outb(self, void):
        self.io[0].VRAM[self.RB] = self.RA

    def load_program(self, program_filename):
        with open(program_filename, "r") as f:
            self.program = f.readlines()[1:][0].replace("\n", "").split(" ")
            self.program.pop(-1)

    def dump_ram(self, cells, verbose):
        if verbose: print(f"[VIRTUAL MACHINE]: DUMPING THE FIRST {cells} RAM CELLS:")
        for i in range(cells):
            end = "|"
            if i % 10 == 0 and i != 0:
                end = "\n"
            print(self.RAM[i], end=end)
        if verbose: print("\n")


    def dump_ra(self, verbose=True):
        if verbose: print(f"[VIRTUAL MACHINE]: DUMPING RA:")
        print(self.RA)

    def dump_rb(self, verbose=True):
        if verbose: print(f"[VIRTUAL MACHINE]: DUMPING RB:")
        print(self.RB)

    def debug(self, cells, verbose=True):
        if verbose: print(f"[VIRTUAL MACHINE]: STARTING DEBUG:")
        self.dump_ram(cells, verbose)
        self.dump_ra(verbose)
        self.dump_rb(verbose)
        if verbose: print(f"[VIRTUAL MACHINE]: ENDING DEBUG.")

    def start_clock(self):
        while True:
            try:
                try:
                    instruction = self.program[self.instruction_pointer]
                except:
                    self.debug(10)
                    exit(0)

                for device in self.io:
                    device.tick()

                #self.debug(1)
                    
                instruction = bin(int(instruction, 16))[2:].zfill(len(instruction)*4)
                instruction = "0000" + instruction

                opcode = instruction[0:8]
                operand = int(instruction[8:24], 2)
                func = self.instruction_macros[self.instructions[opcode]]
                func(operand)
                self.instruction_pointer += 1
            except KeyboardInterrupt:
                self.debug(10)
                exit(1)

        

    