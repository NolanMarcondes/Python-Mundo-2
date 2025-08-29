cont = 0
x = 0
for c in range(1, 7):
    n = int(input('Digite o {} número:'.format(c)))
    if n % 2 == 0:
        x = x + n
        cont = cont + 1
print('Você informou {} números pares e a soma entre eles foi: {}'.format(cont, x))
