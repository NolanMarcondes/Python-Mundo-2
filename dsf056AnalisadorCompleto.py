somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for n in range(1, 5):
    print('----- {}ª PESSOA -----'.format(n))
    nome = str(input('Insira seu nome: ')).strip()
    idade = int(input('Insira sua idade: '))
    sexo = str(input('Insira seu sexo [M/F]: ')).strip()
    somaidade += idade
    if n == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('E também tem {} mulher(s) com menos de 20 anos'.format(mulher))
