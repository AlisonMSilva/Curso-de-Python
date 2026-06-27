""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão"""

print(20 * "=")
print("10 Termos de uma PA")
print(20 * "=")

termo = int(input("Digite um TERMO: "))
razao = int(input("Digite a razão: "))


for c in range(1, 10 + 1):
  print(termo, end=" -> ")
  termo += razao

print("FIM")