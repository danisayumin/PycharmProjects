###triângulos###

a = int(input('digite o valor da reta 1:'))
b = int(input('digite o valor da reta 2:'))
c: int = int(input('digite o valor da reta 3:'))
if b - c < a < b + c or a - c < b < a + c or a - b < c < a + b:
    print('pode forma um triangulo!')
    if a == b == c:
        print("EQUILATERO")
    elif a != b != c:
        print("ESCALENO")
    else:
        print("ISOCELES")

else:
    print(f' nao pode ser um triangulo!')

