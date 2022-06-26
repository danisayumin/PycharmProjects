##ano de alistamento##

nasc = int(input("informe o ano de nascimento: "))
ano = int(input("informe o ano atual: "))

idade = ano-nasc

if idade < 18:
    print("ainda vai se alistar!")
elif idade == 18:
    print("já é hora de se alistar!")
else:
    print("já passou do tempo!")



