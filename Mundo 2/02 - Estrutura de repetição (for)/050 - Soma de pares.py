"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado for ímpar"""


soma = 0
pares = []
contador = 0

for n in range(1, 6 +1):
  n = int(input("Digite um número inteiro: "))

  # Se o número for par
  if n % 2 == 0:
    # Variáveis de controles atualizadas
    soma += n
    contador += 1
    pares.append(n)

if contador == 0:
   print("Todos os números digitados são impares")

elif contador == 1:
  print(f"Apenas um valor digitado foi par, é ele o número 2 {soma}")

else:
  print(f"Foram digitados {contador} números pares, são eles {", ".join(map(str, pares))}")
  print(f"E a soma entre eles é igual a {soma}")