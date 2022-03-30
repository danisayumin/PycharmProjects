v = int(input('qual a distancia em km/h da sua viagem?'))
v1 = v*0.50
v2 = v*0.45
if v < 200:
    print('a sua viagem ira custa R${}'.format(v1))
else:
    print('a viagem ira custar R${}'.format(v2))