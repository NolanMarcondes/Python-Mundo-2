from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
r = 0
while r != 5:
    print('     [1] somar')
    print('     [2] multiplicar')
    print('     [3] maior')
    print('     [4] novos números')
    print('     [5] sair do programa')
    r = int(input('>>>>> Qual é a sua opção? '))
    if r == 1:
        s = n1 + n2
        print(s)
    elif r == 2:
        s = n1 * n2
        print(s)
    elif r == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} maior que {}'.format(n2, n1))
        else:
            print('{} e {} são iguais'.format(n1, n2))
    elif r == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif r == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente Novamente')
    print('=-=' * 17)
    sleep(1)

print('Fim Programa, Volte Sempre!')
