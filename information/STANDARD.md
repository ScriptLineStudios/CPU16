# The Standard Library

The standard library (stdlib.asm) conatins many useful macros that can be used during development. 

## mem -> %imm %addr
The mem macro allows for an immediate value to quickly be loaded into a RAM address.

## push -> %imm
The CPU16 does not have a hardware stack. All stack related operations are simpily macros. The stack starts at memory address 1000 and grows downwards.
The current value of the stack can be accessed using virtual register %RSP. The push operation moves a value into address held by %RSP and then increments it.

## popa -> void
Pops the top value off the stack into %RA

## popb -> void
Pops the top value off the stack into %RB

## drawchar + (a - z) -> void
Draws the sepcified character to the screen with the offset specified by the %OFFSET virtual register
