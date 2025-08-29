#f é a frase
#p são as palavras da frase
#j é a junção das palavras
#i é o inverso
#l são as letras
f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
#i = ''
i = j[::-1]
#for l in range(len(j) - 1, -1, -1):
#    i += j[l]
print('o inverso de {} é {}'.format(j, i))
if i == j:
    print('A frase digitada é Palíndromo')
else:
    print('A frase digitada não é Palíndromo')

