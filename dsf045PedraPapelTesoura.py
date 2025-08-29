from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print(''''Suas opções:
                  [0] PEDRA
                  [1] PAPEL
                  [2] TESOURA''''')
opcao = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
if comp == 0:
    if opcao == 0:
        print('Empate!!')
    elif opcao == 1:
        print('Jogador ganhou!!')
    elif opcao == 2:
        print('Computador ganhou!!')
    else:
        print('OPÇÃO INCORRETA')
elif comp == 1:
    if opcao == 0:
        print('Computador ganhou!!')
    elif opcao == 1:
        print('Empate!!')
    elif opcao == 2:
        print('Jogador ganhou!!')
    else:
        print('OPCAO INCORRETA')
elif comp == 2:
    if opcao == 0:
        print('Jogador ganhou!!')
    elif opcao == 1:
        print('Computador ganhou!!')
    elif opcao == 2:
        print('Empate!!')
    else:
        print('OPCAO INCORRETA')
print('Computador pensou em {}'.format(itens[comp]))
print('Jogador pensou em {}'.format(itens[opcao]))
