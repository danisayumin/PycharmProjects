sexo = str(input('Por favor, informe o seu sexo[M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos.Por favor, informe o seu sexo:[M/F]')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

