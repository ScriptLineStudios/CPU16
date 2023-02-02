&include "standard/stdlib.asm"

mova 65535
draw:
    puts str
    jmp draw
lds:"HELLO WORLD"->str
