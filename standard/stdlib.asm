$drawchara void {
    movb 2+%OFFSET
    outb 0
    movb 34+%OFFSET
    outb 0
    movb 66+%OFFSET
    outb 0
    movb 67+%OFFSET
    outb 0
    movb 68+%OFFSET
    outb 0
    movb 98+%OFFSET
    outb 0
    movb 130+%OFFSET
    outb 0
    movb 3+%OFFSET
    outb 0
    movb 4+%OFFSET
    outb 0
    movb 5+%OFFSET
    outb 0
    movb 37+%OFFSET
    outb 0
    movb 69+%OFFSET
    outb 0
    movb 101+%OFFSET
    outb 0
    movb 133+%OFFSET
    outb 0
    !!%OFFSET++
}

$drawcharb void { 
    movb 2+%OFFSET
    outb 
    movb 34+%OFFSET
    outb 
    movb 66+%OFFSET
    outb 
    movb 98+%OFFSET
    outb 
    movb 130+%OFFSET
    outb 

    movb 3+%OFFSET
    outb 
    movb 36+%OFFSET
    outb 
    movb 67+%OFFSET
    outb 
    movb 100+%OFFSET
    outb 
    movb 131+%OFFSET
    outb 
    !!%OFFSET++
}

$drawcharc void { 
    movb 1+%OFFSET
    outb 
    movb 2+%OFFSET
    outb 
    movb 3+%OFFSET
    outb 
    movb 33+%OFFSET
    outb 
    movb 65+%OFFSET
    outb 
    movb 97+%OFFSET
    outb 
    movb 129+%OFFSET
    outb 
    movb 130+%OFFSET
    outb 
    movb 131+%OFFSET
    outb 
    !!%OFFSET++
}
                
$drawchard void { 
    movb 1+%OFFSET
    outb 
    movb 2+%OFFSET
    outb 
    movb 33+%OFFSET
    outb 
    movb 35+%OFFSET
    outb 
    movb 65+%OFFSET
    outb 
    movb 67+%OFFSET
    outb 
    movb 99+%OFFSET
    outb 
    movb 97+%OFFSET
    outb 
    movb 129+%OFFSET
    outb 
    movb 130+%OFFSET
    outb 
    !!%OFFSET++
}

$drawchare void { 
    movb 1+%OFFSET
    outb 
    movb 2+%OFFSET
    outb 
    movb 33+%OFFSET
    outb 
    movb 65+%OFFSET
    outb 
    movb 66+%OFFSET
    outb 
    movb 97+%OFFSET
    outb 
    movb 129+%OFFSET
    outb 
    movb 130+%OFFSET
    outb 
    movb 131+%OFFSET
    outb
    movb 132+%OFFSET
    outb
    !!%OFFSET++
}

$drawcharf void { 
    movb 0+%OFFSET
    outb 
    movb 1+%OFFSET
    outb 
    movb 32+%OFFSET
    outb 
    movb 64+%OFFSET
    outb 
    movb 65+%OFFSET
    outb 
    movb 96+%OFFSET
    outb 
    movb 128+%OFFSET
    outb 
    !!%OFFSET++
}

$drawcharg void { 
    movb 2+%OFFSET
    outb 
    movb 34+%OFFSET
    outb 
    movb 66+%OFFSET
    outb 
    movb 98+%OFFSET
    outb 
    movb 130+%OFFSET
    outb 
    !!%OFFSET++
}

$drawcharh void { 
    movb 2+%OFFSET
    outb
    movb 34+%OFFSET
    outb
    movb 66+%OFFSET
    outb
    movb 67+%OFFSET
    outb
    movb 68+%OFFSET
    outb
    movb 100+%OFFSET
    outb
    movb 98+%OFFSET
    outb
    !!%OFFSET++
}

$drawchari void { 
    movb 3+%OFFSET
    outb
    movb 2+%OFFSET
    outb
    movb 4+%OFFSET
    outb
    movb 35+%OFFSET
    outb
    movb 67+%OFFSET
    outb
    movb 99+%OFFSET
    outb
    movb 100+%OFFSET
    outb
    movb 98+%OFFSET
    outb
    !!%OFFSET++
}
            
$drawcharj void { 
    movb 3+%OFFSET
    outb
    movb 35+%OFFSET
    outb
    movb 67+%OFFSET
    outb
    movb 99+%OFFSET
    outb
    movb 100+%OFFSET
    outb
    movb 69+%OFFSET
    outb
    !!%OFFSET++
}

$drawchark void { 
    movb 3+%OFFSET
    outb
    movb 35+%OFFSET
    outb
    movb 36+%OFFSET
    outb
    movb 69+%OFFSET
    outb
    movb 101+%OFFSET
    outb
    movb 5+%OFFSET
    outb
    movb 67+%OFFSET
    outb
    movb 99+%OFFSET
    outb
    !!%OFFSET++
}

$drawcharl void { 
    movb 3+%OFFSET
    outb
    movb 35+%OFFSET
    outb
    movb 67+%OFFSET
    outb
    movb 99+%OFFSET
    outb
    movb 100+%OFFSET
    outb
    !!%OFFSET++
}

$drawcharm void { 
    movb 3+%OFFSET
    outb
    movb 4+%OFFSET
    outb
    movb 37+%OFFSET
    outb
    movb 6+%OFFSET
    outb
    movb 7+%OFFSET
    outb
    movb 39+%OFFSET
    outb
    movb 71+%OFFSET
    outb
    movb 103+%OFFSET
    outb
    movb 35+%OFFSET
    outb
    movb 67+%OFFSET
    outb
    movb 99+%OFFSET
    outb
    !!%OFFSET++
}

$drawcharn void { 
    movb 3+%OFFSET
    outb
    movb 4+%OFFSET
    outb
    movb 37+%OFFSET
    outb
    movb 69+%OFFSET
    outb
    movb 101+%OFFSET
    outb
    movb 35+%OFFSET
    outb
    movb 67+%OFFSET
    outb
    movb 99+%OFFSET
    outb
    !!%OFFSET++
}

$push %x {
    mova %x
    ldia %RSP
    !!%RSP++
}

$popa void { {
    !!%RSP--
    lda %RSP
}

$popb void { {
    !!%RSP--
    ldb %RSP
}

$mem %imm %addr {
    mova %imm
    ldia %addr
}
