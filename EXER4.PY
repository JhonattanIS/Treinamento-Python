'''
Escreva um programa que leia um número real e mostre na tela os valores de 25%, 50%, 75% do 
valor lido usando o formato com 3 casas decimais mostrado abaixo: 
Exemplo
Valor lido: 136.7 
Exibir 25% -> 34.175   -   50% -> 68.350   -   75% -> 102.525 '''

#recebe o valor e converte para float
a = float(input("valor a ser lido:"))
#faz os calculos com o valor
b = (a/100)*25
c = (a/100)*50
d = (a/100)*75
#limita 3 casas decimais
BF = "{:.3F}".format(b)
CF = "{:.3F}".format(c)
DF = "{:.3F}".format(d)
#organiza o print com as porcentagens
A = f"25% -> {BF}"
B = f"    50% -> {CF}"
C = f"    75% -> {DF}"
#exibe os valores
print (A, B, C) 