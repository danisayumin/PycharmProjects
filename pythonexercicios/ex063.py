termos = int(input('Quantos termos voce gostaria de mostrar?:'))
t1 = 0
t2 = 1
print(t1, t2, end="-")
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(t3, end="-")
    t1 = t2
    t2 = t3
    cont += 1
print('fim')

