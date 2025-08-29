from datetime import date
atual = date.today().year
s = 0
for pess in range(1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu: '.format(pess)))
    idd = atual - n
    if idd < 21:
        s += 1
ma = 7 - s
print('Ao todo tivemos {} pessoas maiores de idade'.format(ma))
print('E também tivemos {} pessoas menores de idade'.format(s))
