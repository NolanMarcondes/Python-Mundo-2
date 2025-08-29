from random import randint
#from time import sleep
computador = randint(0, 10)
print('-=-'*20)
print('Vou pensar em um número de 0 a 10 e você terá que adivinhar...')
print('-=-'*20)
n = int(input('Digite qual o número que eu estou pensando:'))
while n != computador:
    if n > computador:
        n = int(input('Menos!! Digite um número novamente: '))
    if n < computador:
        n = int(input('Mais!! Digite um número novamente: '))
    if n == computador:
        print('Parabéns!! você acertou')
