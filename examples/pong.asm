&include "standard/stdlib.asm"

mem 0 0 ;player 1
mem 31 1 ;player 2

mova 65535
loop:
    pp:
        mova 97
        inb
        jmp pp

    mova 0
    ldb 0 ;clear player 1
    outb

    lda 0
    movb 32 ; update player 1 pos
    add
    ldia 0

    mova 65535
    ldb 0 ;render player 1
    outb

    ldb 1 ;render player 2
    outb

    pushb
    jmp loop