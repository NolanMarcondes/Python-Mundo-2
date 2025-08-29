N1 = int(input('Digite um número:'))
N2 = int(input('Digite outro número:'))
if N1 > N2:
    print('{} é maior que {}!'.format(N1, N2))
elif N1 < N2:
    print('{} é menor que {}!'.format(N1,N2))
else:
    print('Não existe valor maior, os dois são iguais!')
