from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu?'))
x = atual - nasc
if x == 18:
    print('Já está na hora de se alistar!!')
elif x < 18:
    f = 18 - x
    ano = atual + f
    print('faltam {} ano(s) para você se alistar!'.format(f))
    print('Seu alistamento será em {}'.format(ano))
else:
    f = x - 18
    ano = atual - f
    print('Já passou {} ano(s) do seu alistamento!'.format(f))
    print('Seu alistamento foi em {}'.format(ano))
