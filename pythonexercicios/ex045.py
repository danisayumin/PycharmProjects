from random import randint

itens = ("pedra","papel","tesoura")
comput = randint(0, 2)
print("""Escolha uma opção:
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura""")
player = int(input("escolha uma opção: "))
print("-="*11)
print(f"o computador jogou {itens[comput]}")
print(f"o jogador jogou {itens[player]}")
print("-="*11)

if comput == 0 : #computador joga pedra
    if player == 0:
        print("empate!")
    elif player == 1:
        print("jogador venceu !")
    elif player == 2:
        print("computador venceu!")

elif comput == 1 : #computador joga papel
    if player == 0:
        print("computador venceu!")
    elif player == 1:
        print("empate! ")
    elif player == 2:
        print("jogador venceu!")

elif comput == 2 :
    if player == 0:
        print("jogador venceu!")
    elif player == 1:
        print("empate!")
    elif player == 2:
        print("computador venceu!")