from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
v = 0
while True:
    n = int(input('Diga um valor: '))
    computador = randint(0, 10)
    t = n + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {computador}. total de {t}', end=' ')
    print('DEU PAR' if t % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if t % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if t % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente... ')
print(f'GAME OVER! Você venceu {v} vezes')
