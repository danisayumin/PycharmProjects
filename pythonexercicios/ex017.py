from math import hypot
co = float(input('digite o cateto oposto:'))
ca = float(input('digite o cateto adjacente:'))
hi = hypot(co, ca)
print('o comprimento da hipotenusa do triangulo retangulo será de {:.2f}'.format(hi))
