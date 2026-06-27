"""Crie um programa que mostre na tela todos os números pares que estão no 
intervalo entre 1 e 50"""

print("\033[32mMostrando apenas valores PARES\033[m")

inicio = int(input("Digite um número de partida: "))
fim = int(input("Digite o número final: "))

for par in range(inicio, fim + 1):
  if par % 2 == 0:
    print(par)

print("ACABOU")