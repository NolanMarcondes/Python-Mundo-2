n = int(input('Digite um número para calcular seu fatorial: '))
s = n
f = 1

print('Calculando {}! = '.format(n), end='')
while s > 0:
    print('{}'.format(s), end='')
    print(' x ' if s > 1 else ' = ', end='')
    f *= s
    s -= 1
print('{}'.format(f))
