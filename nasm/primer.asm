section .data
    msg db 'hola', 10

section .text
    global main
    main:
    mov rax, 4
    mov rbx, 1
    mov rcx, msg
    mov rdx, 6
    int 80h
    mov rax, 1
    mov rbx, 0
    int 80h
    