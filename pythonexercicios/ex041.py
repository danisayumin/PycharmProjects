##categoria de atleta##

nasc = int(input("Em que ano você nasceu? "))
ano = int(input("Em que ano estamos? "))

idade = ano-nasc

if idade <= 9 :
    print("categoria: MIRIM")
elif idade <= 14:
    print("categoria: INFANTIL")
elif idade <= 19:
    print("categoria: JUNIOR")
elif idade <= 20:
    print("categoria: SÊNIOR")
elif idade > 20:
    print("categoria: MASSTER")
