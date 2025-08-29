print('Gerador de PA')
print('-=' * 10)
x = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
while cont <= 10:
    print('{} '.format(x), end="-> ")
    x += razao
    cont += 1
print('FIM')
