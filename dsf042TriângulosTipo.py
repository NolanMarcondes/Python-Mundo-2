a = float(input('Primeiro Seguimento:'))
b = float(input('Segundo Seguimento:'))
c = float(input('Terceiro Seguimento:'))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Pode formar um Triângulo!')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Não pode formar um Triângulo!')
