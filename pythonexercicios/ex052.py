num = int(input("Digite um número:"))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[34m", end=" ")
        tot += 1
    else:
        print("\033[33m", end=" ")
    print(f"{c}", end=" ")
print(f"o numero {num} foi divisivel {tot} vezes")
if tot == 2:
    print("por isso ele é primo!")
else:
    print("e por isso ele não é primo!")
