sal = float(input('quanto é o seu salario atual?'))
if 1250.00 < sal:
    print(f'o aumento do seu salario de {sal} ficara {(sal * 10 / 100) + sal} ')
else:
    print(f'o aumento do seu salario de {sal} ficara {(sal * 15 / 100) + sal}')
