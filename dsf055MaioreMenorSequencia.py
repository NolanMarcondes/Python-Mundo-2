#hp = maior peso
#lp = menor peso
#n = número de pessoas
#p = peso

hp = 0
lp = 0

for n in range (1, 6):
    p = float(input('Peso da {}ª pessoa: '.format(n)))
    if n == 1:
        hp = p
        lp = p
    else:
        if p > hp:
            hp = p
        if p < lp:
            lp = p
print('O maior peso lido foi de {}KG'.format(hp))
print('O menor peso lido foi de {}KG'.format(lp))
