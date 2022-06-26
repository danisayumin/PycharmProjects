##valor a ser pago ##

val = float(input("informe o preço normal das compras: "))
print("""condição de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("qual é a opção?"))
if opcao == 1 :
    total = val - (val * 10/100)
elif opcao == 2 :
    total = val - (val * 5/100)
elif opcao == 3 :
    total = val
    parcela = total/2
    print(f"Sua conta sera parcelada em 2x de {parcela} sem JUROS")
elif opcao == 4:
    total = val +(val*20/100)
    totparc = int(input("quantas parcelas?"))
    parcela = total / totparc
    print(f"sua compra sera parcelada em {totparc}x de R${parcela} com JUROS")
else:
    total=0
    print("Opção invalida de pagamento.Tente novamente")
print(f"sua compra de {val} vai custar R${total} no final.")
