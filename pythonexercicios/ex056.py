somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1,5):
    nome = str(input(f"Qual o nome da {p} pessoa?"))
    idade = int(input(f"Quantos anos {p} pessoa tem?"))
    sexo = str(input(f"A pessoa possui o sexo :\n Masculino?(M) \n Feminino(F)"))
    somaidade += idade
    if p == 1 and sexo in "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "F" and idade < 20:
        totmulher20 += 1
media = somaidade / 4
print(f"A média de idade do grupo é de {media}")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")
