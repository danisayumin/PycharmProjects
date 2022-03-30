import math
angulo = float(input('digite o angulo que vc deseja:'))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o SENO de {:.2}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {} tem COS de {:.2}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem a TAN de {:.2}'.format(angulo,tangente))