""" Faça um algoritmo que determina a categoria de um lutador a partir de seu peso, seguindo a tabela abaixo:
Não pode lutar | Menor que 53kg
super leve     | maior que 53kg, menor que 60
leve           | maior que 60kg, menor que 70
medio          | maior que 70kg, menor que 80
pesado         | maior que 80kg, menor que 90
peso pesado    | maior que 90kg
"""

Nome = input('Nome do lutador: ')
peso = float(input("peso do lutador: "))
if peso < 53 :
    print ("Lutador não está apto")
elif peso > 53 and peso < 60:
     print(f"{Nome} está na categoria Super leve com peso de {peso}")
elif peso > 60 and peso < 70:
     print(f"{Nome} está na categoria Leve com peso de {peso}")
elif peso > 70 and peso < 80:
     print(f"{Nome} está na categoria Média com peso de {peso}")
elif peso > 90:
     print(f" {Nome} está na categoria Pesado com peso de {peso}")
         
