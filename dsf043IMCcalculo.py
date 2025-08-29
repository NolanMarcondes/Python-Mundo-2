peso = float(input('Qual é o seu peso?'))
alt = float(input('Qual a sua altura?'))
IMC = peso / (alt**2)
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você esta ABAIXO DO PESO!')
elif IMC < 25:
    print('PARABÉNS! Você está no peso ideal')
elif IMC < 30:
    print('Você está Sobrepeso...')
elif IMC <= 40:
    print('Vai se cuidar!! você está com obesidade...')
else:
    print('OBESIDADE MÓRBIDA!!! Busque por um médico agora!!!!')
