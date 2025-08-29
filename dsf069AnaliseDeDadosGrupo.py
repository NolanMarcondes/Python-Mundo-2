cont = homem = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        cont += 1
    if sexo in 'Mm':
        homem += 1
    if continuar in 'N':
        break
print(f'Existem {homem} homem(s) cadastrado(s) e {cont} pessoa(s) maior(s) de 18 anos')
