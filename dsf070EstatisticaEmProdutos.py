print('-' * 30)
print('LOJÃO DO NOLAN')
print('-' * 30)
total = contmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    total += preco
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if preco > 1000:
        contmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if continuar == 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total gasto foi de R${total:.2f} e {contmil} produtos custaram mais de R$1000,00')
print(f'O produto mais barato foi {barato} e o valor dele é de R${menor:.2f}')