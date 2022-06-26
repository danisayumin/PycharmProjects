## IMC ##

kg = float(input("digite seu peso em kg: "))
m = float(input("digite sua altura em metros^2: "))

IMC = kg/m

if IMC < 18.5:
    print("Esta abaixo do peso!")
elif 18.5>=IMC<=25 :
    print("Peso ideal")
elif 25>=IMC<=30 :
    print("Sobrepeso")
elif 30 >=IMC<=40:
    print("Obesidade")
else:
    print("Obesidade mórbida")