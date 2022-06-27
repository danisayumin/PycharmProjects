num = 0
opcao ="S"
cont = 0
soma = 0
maior = 0
menor = 0
while opcao in "Ss":
    num = int(input("digite um número:"))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input("Quer continuar[S/N]?")).upper().strip()[0]
med = soma/cont
print(f"A média entre os numeros é de {med}")
print(f"o maior numero foi {maior} e o menor foi {menor}")