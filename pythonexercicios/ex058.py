import random
num = random.randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    adv = int(input('qual seu palpite:'))
    palpites += 1
    if adv == num:
        acertou = True
print('voce advinhou !')
print(f"o numero de palpites foram {palpites} para acertar o numero {num}")