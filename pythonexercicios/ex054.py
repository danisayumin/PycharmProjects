from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input(f"em que ano a {pess} pessoa nasceu?"))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
print(f"Ao todo tivemos {totmaior} pessoas maiores ")
print(f"Ao todo tivemos {totmenor} pessoas menores")