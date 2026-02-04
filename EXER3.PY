"""
Escreva um programa que leia três números reais em objetos denominados A, B e C. O programa 
deve calcular e mostrar na tela os resultados das fórmulas a seguir, usando 3 casas decimais. 

 R1=A+B+C R2=AxBxC R3=2x(A+B)-C R4=(A+B+C)/3 R5=(2xB+3xC)/(5xA) R6=A^2+B^2

Para testar seu programa considere: A = 22.65    B = –39.1    C = 18.115 
R1 = 1.665 
R2 = –16042.916 
R3 = –51.015 
R4 = 0.555 
R5 = –0.211 
R6 = 2041.832 
"""
#digita os valores das variaveis, já converte em float.
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
#Calcula os valores.
R1 = a+b+c
R2 = a*b*c
R3 = 2*(a+b)-c
R4 = (a+b+c)/3
R5 = (2*b+3*c)/(5*a)
R6 = a**2+b**2
#Limita os resultados em 3 casas decimais.
R1F = "{:.3F}".format(R1)
R2F = "{:.3F}".format(R2)
R3F = "{:.3F}".format(R3)
R4F = "{:.3F}".format(R4)
R5F = "{:.3F}".format(R5)
R6F = "{:.3F}".format(R6)
#salva os valores limitados em uma variavel.
A = "R1={}  R2={}  R3={}  R4={}  R5={}  R6={} " .format(R1F, R2F, R3F, R4F, R5F, R6F)
#exibe a variavel
print (A)