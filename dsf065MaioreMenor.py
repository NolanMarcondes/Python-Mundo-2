continuar = 'S'
soma = quant = media = maior = menor = 0
while continuar in 'Ss':
    n1 = int(input('Digite um número: '))
    soma += n1
    quant += 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > menor:
            maior = n1
        if n1 < menor:
            menor = n1
    media = soma / quant
    continuar = str(input('Quer continuar? [S/N] '))
print('O maior valor digitado foi {} e o menor valor digitado foi {}'.format(maior, menor))
print('A média entre todos os valores foi {}'.format(media))
