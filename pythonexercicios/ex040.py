###média de notas###

p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota : "))

m = (p1+p2)/2

if m < 5.0:
    print("REPROVADO")
elif m == 5.0 and 6.9:
    print("RECUPERAÇÃO")
elif m >= 7.0:
    print("APROVADO")

