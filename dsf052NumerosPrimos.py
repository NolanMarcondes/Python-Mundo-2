n = int(input('Digite um número: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        s += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, s))
if s == 2:
    print('E por isso ele é Primo'.format(n))
else:
    print('E por isso ele não é Primo'.format(n))
