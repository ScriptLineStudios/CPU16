$push %x {
    mova %x
    ldia %RSP
    !!%RSP++
}

$popa void {
    lda %RSP
    !!%RSP--
}

$popb void {
    ldb %RSP
    !!%RSP--
}

$mem %imm %addr {
    mova %imm
    ldia %addr
}

mem 0 0
mem 1 1
mem 0 2
fibb:
    lda 0
    ldb 1
    add
    ldia 2
    lda 1
    ldia 0
    lda 2
    ldia 1
    jmp fibb