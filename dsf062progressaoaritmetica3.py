print('Gerador de PA')
print('-=' * 10)
x = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
total = 0
r = 10
while r != 0:
    total += r
    while cont <= total:
        print('{} '.format(x), end="-> ")
        x += razao
        cont += 1
    print('PAUSA')
    r = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
