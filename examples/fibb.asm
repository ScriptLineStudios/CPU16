&include "standard/stdlib.asm"
mova 20
movb 2

ldib 0 ;; This will be decremented each time

ldia 1 ;;This is A
ldib 2 ;;This is B
mul:
    lda 1
    ldb 2 ;; This will 
    add 
    ldia 1

    lda 0
    movb 1
    sub
    ldia 0
    jnz mul

lda 1