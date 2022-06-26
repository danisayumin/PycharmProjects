#emprestimo bancario

casa = float(input('qual o valor da casa? '))
sal = float(input('qual o valor do salario do comprador? '))
anos = int(input('em quantos anos ele ira pagar?'))

parcela = casa/(anos*12)

if parcela>30/100*sal:
    print('a prestação excedeu 30% do seu salário , o empréstimo foi negado')

else :
    print(f'empréstimo confirmado, o valor será de {parcela}!')


