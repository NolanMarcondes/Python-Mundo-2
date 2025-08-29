from time import sleep
print('='*11, 'LOJA DO NOLAN', ('='*11))
preco = float(input('Preço das compras:'))
print(''''FORMAS DE PAGAMENTOS:
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
sleep(1)
if opcao == 1:
    x = preco - (10/100 * preco)
    print('Você terá que pagar R${:.2f} e o desconto foi de 10%'.format(x))
elif opcao == 2:
    x = preco - (5/100 * preco)
    print('Você terá que pagar R${:.2f} e o desconto foi de 5%'.format(x))
elif opcao == 3:
    print('Você terá que pagar R${:.2f}'.format(preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    x = preco + (20/100 * preco)
    y = x / parcelas
    print('Você terá que pagar R${:.2f} parcelado em {} vezes de R${:.2f}'.format(x, parcelas, y))
else:
    print('OPÇAO INCORRETA!!')
