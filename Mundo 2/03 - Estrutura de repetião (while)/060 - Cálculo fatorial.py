"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120"""

print("\033[1;37mDigite um número inteiro\033[m")
numero = input("Para calcular seu fatorial: ")

# Validação
while not numero.isdigit():
  numero = input("Digite apenas números inteiro: ")

numero = int(numero) + 1
resultado = 1


print(f"{numero - 1}! = ", end=" ")

while numero > 1:
  numero  -= 1 

  resultado = resultado * numero

  if numero > 1:
    print(numero, end=" X " )
  else:
    print(f"1 = ", end="")

print(resultado)