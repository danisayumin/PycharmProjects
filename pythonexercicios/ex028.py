# faz o programa advinhar em um numero
# from random import randint
import random
num = random.randint(0,5)
adv = int(input('advinhe o numero pensado de 0-5:'))
if adv == num:
    print('voce advinhou !')
else :
    print('o numero pensado foi {} ,nao {}.O computador venceu!'.format(num,adv))