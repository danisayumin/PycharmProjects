termo = int(input("primeiro termo: "))
razao = int(input("Razão: "))
termo1 = termo
cont = 1
while cont <= 10:
    print(f"{termo1}", end="->")
    termo1 += razao
    cont += 1
print("acabou")

