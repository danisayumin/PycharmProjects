v = int(input('quantos km/h voce esta?'))
multa = (v-80)*7
if v>80:
    print('VOCE FOI MULTADO EM R${}!'.format(multa))
else :
    print('ta limpo!')