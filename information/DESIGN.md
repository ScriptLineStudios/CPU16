# CPU16 Design Doc

# Memeory

## Registers:
	1. RA  - General Purpose 16bit Register
	2. RB  - General Purpose 16bit Register
	3. RZ  - Zero flag gets updated automatically returns 1 if RA is > 0 and 0 is RA = 0
	4. RSP - Virtual Stack Pointer (View Section: The Stack)
## RAM:
	1. 0x0000 --> 0x7999  - General RAM space for programs to use
	2. 0x8000 --> 0x10000 - Reserved stack space

# Instructions

Note: All instructions are 8 bit and take 16 bit operands for example XXXXXXXXYYYYYYYYYYYYYYYY

1.  MOVA - Moves an immediate into the RA register                                              
2.  MOVB - Moves an immediate into the RB register
3.  LDIA - Loads the contents of RA register into the specified ram address
4.  LDIB - Loads the contents of RB register into the specified ran address
5.  ADD  - Adds the contents of RA and RB and puts the result in RA 
6.  SUB  - Subtracts the contents of RA and RB and puts the result in RA. (TODO: Negative numbers)
7.  JMP  - Jumps unconditionally to a specified line
8.  JNZ  - Jumps if the contents of RZ is not 0
9.  LDA  - Loads RA with the contents of the specified address
10. OUTB - Outputs the contents of RA to the VRAM

# The Stack

The CPU16 does not have a hardware stack. All stack releated calculations are done at assemble time. The stacks memory starts at 
0x8000 and can grow until 0x100000 (View Section: Memory). The assembler keeps track of where the stack pointer is located using a
virtual register called RSP which similar to all other registers can be referred to in programs.

# Macros

Note: The CPU16 assembler supports macros which are instructions which get broken down into instructions described above

1. PUSH - Pushes an immediate to the stack               (%imm        --> MOVA %imm, LDIA %RSP)
2. POP  - Pops top value off the stack and stores in RA  (void        --> LDA %RSP)
3. MEM  - Loads a value directly into an address         (%addr, %imm --> MOVA %imm, LDIA %addr)

# Control Unit
Note: Format is denoted using the following: Instruction(8 bits) + Instruction Count(2 bits)

MOVA:
	00000001 OO, AI      --> 00010000000100 (0x204)
	00000001 NONE 	     --> 00000000000000 (0x0)
	00000001 NONE        --> 00000000000000 (0x0)
	00000001 CE          --> 00100000000000 (0x800)
MOVB:
	00000010 OO, BI      --> 00010000001000 (0x208)
	00000010 NONE        --> 00000000000000 (0x0)
	00000010 NONE        --> 00000000000000 (0x0)
	00000010 CE          --> 00100000000000 (0x800)
LDIA:
	00000011 OO, MI      --> 00010000010000 (0x208)
	00000011 AO, RI      --> 00000000100001 (0x0)
	00000011 NONE        --> 00000000000000 (0x0)
	00000011 CE          --> 00100000000000 (0x800)
LDIB:
	00000100 OO, MI      --> 00010000010000 (0x208)
	00000100 BO, RI      --> 00000000100010 (0x0)
	00000100 NONE        --> 00000000000000 (0x0)
	00000100 CE          --> 00100000000000 (0x800)
ADD:
	00000101 ALUA        --> 00000100000000 (0x208)
	00000101 ALUO, AI    --> 00000010000100 (0x0)
	00000101 NONE        --> 00000000000000 (0x0)
	00000101 CE          --> 00100000000000 (0x800)
SUB:
	00000110 ALUA        --> 00001000000000 (0x208)
	00000110 ALUO, AI    --> 00000010000100 (0x0)
	00000110 NONE        --> 00000000000000 (0x0)
	00000110 CE          --> 00100000000000 (0x800)
JMP: 
	00000111 LADDER      --> 01000000000000 (0x208)
	00000111 NONE        --> 00000000000000 (0x0)
	00000111 NONE        --> 00000000000000 (0x0)
	00000111 CE          --> 00000000000000 (0x800)
JNZ: --> IF THE CONTENTS OF THE CMP = 0 WE DO NOTHING, OTHER WISE WE EXECUTE A JUMP INSTRUCTION AS ABOVE. THE BELOW SHOWS THE JUMP STATE:
	00001000 LADDER      --> 01000000000000 (0x208)
	00001000 NONE        --> 00000000000000 (0x0)
	00001000 NONE        --> 00000000000000 (0x0)
	00001000 CEE         --> 00100000000000 (0x800)
LDA: 
	00001001 OO, MI      --> 00001000001000 (0x208)
	00001001 RO, AI      --> 00000000000000 (0x0)
	00001001 NONE        --> 00000000000000 (0x0)
	00001001 CE          --> 00100000000000 (0x800)
LDB: 
	00001010 OO, MI      --> 0001000001000 (0x208)
	00001010 RO, BI      --> 00000000000000 (0x0)
	00001010 NONE        --> 00000000000000 (0x0)
	00001010 CE          --> 00100000000000 (0x800)
OUTB:
	00001011 AW          --> 10000000000000 (0x208)
	00001011 NONE        --> 00000000000000 (0x0)
	00001011 NONE        --> 00000000000000 (0x0)
	00001011 CE          --> 00100000000000 (0x800)


1  = RA OUT
2  = RB OUT
3  = RA IN
4  = RB IN
5  = MAR IN
6  = RAM IN
7  = RAM OUT
8  = ALU OUT
9  = ALU ADD
10 = ALU SUB
11 = OO
12 = CE
13 = LADDER
14 = CCE (Conditional counter enable -> if ZF != 0 then enables load signal, other just enables)

