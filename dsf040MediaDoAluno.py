n1 = float(input('Qual a primeira nota do aluno?'))
n2 = float(input('Qual a segunda nota do aluno?'))
md = (n1 + n2) / 2
if md < 5:
    print('Reprovado!')
elif md >= 7:
    print('Aprovado!')
else:
    print('Recuperação!')
