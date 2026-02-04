"""Exercício Proposto 3.1  
Enunciado: 
Escreva um programa que leia os nomes de três pessoas de uma família: mãe, pai e criança. O 
programa deve exibir na tela a mensagem. 
"Os adultos {mãe} e {pai} são os responsáveis por {criança}" 
Faça de dois modos: com o método .format() e com f-string """

print ('qual o nome do pai? ')
a = input ('nome do pai: ')
print ("qual o nome da mãe? ")
b = input ('nome do mãe: ')
print ("qual o nome do filho? ")
c= input ("nome do filho: ")
d = "Os adultos {} e {} são os responsáveis por {}." .format (b, a, c)  #método  .format()
e = f"Os adultos {b} e {a} são os responsáveis por {c}."                #método  f-string
print (d)                                                               #resposta .format
print (e)                                                               #resposta f-string   