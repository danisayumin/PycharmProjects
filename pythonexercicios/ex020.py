import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('segubndo aluno:'))
lista = [n1, n2]
random.shuffle(lista)
print('a ordem sera ')
print(lista)