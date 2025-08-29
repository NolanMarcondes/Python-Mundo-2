x = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
limite = x + (10 - 1) * razao
for c in range(x, limite + razao, razao):
    x = x + razao
    print('{} '.format(c), end="-> ")
print('ACABOU')
