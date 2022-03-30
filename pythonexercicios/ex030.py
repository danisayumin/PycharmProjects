#par ou impar
num: int = int(input('diite um numero e direi se é par ou impar!:'))
pi = num % 2
if pi == 0:
    print('{} é par'.format(num))
else:
    print('é impar!')
