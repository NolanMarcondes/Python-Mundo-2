sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
'''if sexo == 'Mm':
    print('Sexo Masculino registrado com sucesso')
if sexo == 'Ff':
    print('Sexo Feminino registrado com sucesso')'''