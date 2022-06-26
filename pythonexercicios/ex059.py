valor1 = int(input('digite um valor:'))
valor2 = int(input('digite um valor:'))
opcao = 0
while opcao != 5:
    opcao = int(input("""DIGITE UMA DAS OPÇOES 
             [1] somar
             [2] multiplicar
             [3] maior
             [4] novos numeros
             [5] sair do programa"""))
    if opcao == 1:
        soma = valor1+valor2
        print(f'a soma entre os numeros é de {soma}')
    elif opcao == 2:
        multiplo = valor1*valor2
        print(f'o multiplo desses numeros é de {multiplo}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'o valor {valor1} é maior')
        else:
            print(f'o valor {valor2} é maior')
    elif opcao == 4:
        valor1 = int(input('Digite um novo valor:'))
        valor2 = int(input('Digite um novo valor:'))
    elif opcao == 5:
        print('obrigada por utilizar o programa :)')
    else:
        print('opção invalida.Tente novamente')
print('fim do programa')