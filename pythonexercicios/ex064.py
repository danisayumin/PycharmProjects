cont = 0
num = 0
soma = 0
num = int(input('Digite um numero[999 para encerrar]:'))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero[999 para encerrar]:'))
    
print(f'voce digitou {cont} numeros e a soma entre eles deu {soma}')