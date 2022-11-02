mem 0 0 ; a
mem 1 1 ; b
mem 0 2 ; c
fibb:
    lda 0
    ldb 1 ;; CREATES NEW FIBB NUMBER
    add
    ldia 2 ;;MOVES THE NEW NUMBER INTO C
    lda 1
    ldia 0
    lda 2
    ldia 1
    jmp fibb