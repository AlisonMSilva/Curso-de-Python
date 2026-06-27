"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo."""
# 📌 Pegue o maior lado e veja se ele é menor que a soma dos outros dois.

from utils import cores
print("-=" * 30)
print("Analisador de triângulos")
print("-=" * 30)

A = float(input("Digite o 1° segmento: "))
B = float(input("Digite o 2° segmento: "))
C = float(input("Digite o 3° segmento: "))

if A + B > C and A + C > B and B + C > A:
  analisador = f"{cores.VERDE}PODEM FORMAR{cores.RESET}"

else:
  analisador = f"{cores.VERMELHO}NÃO PODEM FORMAR{cores.RESET}"

print(f"Os seguimentos acima {analisador} um triângulo")