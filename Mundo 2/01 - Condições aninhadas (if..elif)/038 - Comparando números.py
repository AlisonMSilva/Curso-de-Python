""" 
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""

n1 = int(input("Digite o 1° valor inteiro: "))
n2 = int(input("Digite o 2° valor inteiro: "))

if n1 > n2:
  print(f"{n1} é o MAIOR!")

elif n2 > n1:
  print(f"{n2} é o MAIOR!")

elif n1 == n2:
  print(f"Os dois valores são IGUAIS!")