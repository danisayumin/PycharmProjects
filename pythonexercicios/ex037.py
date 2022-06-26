num = int(input('digite um número inteiro: '))
print('''Escolha uma das bases para conversao:
 [1] converter para BINÁRIO
 [2] converter para OCTAL
 [3] converter para HEXADECIMAL''')
opcao = int(input('sua opção: '))

bi = str(bin(num))
bi = bi[2:]
oc = str(oct(num))
oc = oc[2:]
he = str(hex(num))
he = he[2:]

if opcao == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bi}")
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oc}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {he}')
else:
    print('opção invalida.Tente novamente')


