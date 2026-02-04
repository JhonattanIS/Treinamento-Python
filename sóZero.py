i = 1
b = 0
while i != 0:
    a = int(input("Digite um número: "))
    if a == 0:
        print(f"O número está correto, a soma final foi de {b}")
        break
    else:
        b = b + a
        print("Número errado")