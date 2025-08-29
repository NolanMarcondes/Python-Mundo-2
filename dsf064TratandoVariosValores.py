n = 0
r = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        r += n
        cont += 1
print('Você digitou {} números e a soma de todos eles foi {}'.format(cont, r))
