termo = int(input("primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10-1)*razao
for c in range(termo, decimo + razao, razao):
    print(f"{c}", end="->")
print("acabou")