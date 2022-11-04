&include "standard/stdlib.asm"

mova 65535
loop:
    movb 1
    sub 
    puts str
    jmp loop

lds:"HELLO WORLD"->str