#####condicionais aninhada#########

nome = str(input('qual é o seu nome '))
if nome == 'Daniela':
    print('que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('belo nome feminino!')
else:
    print('seu nome é bem normal')
print(f'tenha um bom dia,{nome}')