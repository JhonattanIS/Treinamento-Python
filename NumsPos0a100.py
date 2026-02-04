
d = int(input("Digite um número: "))
cont = 1
if d > 0:
    while cont < 100:
        if cont % d == 0:
            print (cont, end=" ")
            cont = cont + 1
        else:
            cont = cont + 1
else:
    print ("Número inválido")
    
print ("\n\nFim")
        