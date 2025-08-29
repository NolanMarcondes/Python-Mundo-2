N = int(input('Qual número inteiro você quer converter?'))
print('''Qual base quer converter:'
[1] para Binário
[2] para Octal 
[3] para Hexadecimal''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {} '.format(N, bin(N)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(N, oct(N)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(N, hex(N)[2:]))
else:
    print('Opção nao existe')
