from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento:'))
idade = atual - ano
if idade <= 9:
    print('Classificação:MIRIM')
elif idade <= 14:
    print('Classificação:INFANTIL')
elif idade <= 19:
    print('Classificação:JÚNIOR')
elif idade <= 25:
    print('Classificação:SÊNIOR')
else:
    print('Classificação:MASTER')
