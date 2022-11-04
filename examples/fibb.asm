&include "standard/stdlib.asm"

mova 65535
loop:
    puts str
    jmp loop

lds:"HELLO WORLD"->str