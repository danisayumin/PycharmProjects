termo = int(input("primeiro termo: "))
razao = int(input("Razão: "))
termo1 = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo1}", end="-")
        termo1 += razao
        cont += 1
    print("pausa")
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressao finalizada com {total} termos mostrados')

