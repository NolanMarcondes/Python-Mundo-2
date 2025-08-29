#MeuPrograma
casa = float(input('Qual o valor da casa?'))
sal = float(input('Quanto você recebe de salário?'))
tempo = int(input('Em quantos anos você vai pagar a casa?'))
x = casa / (tempo * 12)
if x > (sal * 0.3):
    print('Empréstimo negado a prestação é de R${:.2f} e excede 30% do seu salário'.format(x))
else:
    print('O valor mensal que se deve pagar de empréstimo é de R${:.2f}!'.format(x))
