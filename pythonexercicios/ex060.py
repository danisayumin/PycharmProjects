n = int(input('Digite um numero:'))
c = n
f = 1
print(f'o fatorial de {n}!')
while c > 0:
    print(c, end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f)