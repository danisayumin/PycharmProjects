l = float(input('A largura da parede:'))
h = float(input('A altura da parede:'))
A = h*l
T = A/2
print('Sua parede tem dimensao de {}x{} e sua area é {}m'.format(l,h,A))
print('precisa de {}l de tinta para pintar a parede toda'.format(T))