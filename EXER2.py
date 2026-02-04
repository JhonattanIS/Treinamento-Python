'''
Escreva um programa que leia um texto e mostre na tela o texto e a quantidade de caracteres que 
ele contém, usando a seguinte mensagem: 
"O texto {AquiColoqueOTexto} contém {Quantidade} caracteres" 
Faça de dois modos: com o método .format() e com f-string 
Use a função len() '''

a = input ("Escreva um texto:\n")
b = len (a)
c = f"o texto {a} contém  {b} caracteres"                            #método  f-stringd 
d = "o texto {} contém  {} caracteres" .format(a, b)                 #método  .format()
print (c)
print (d)