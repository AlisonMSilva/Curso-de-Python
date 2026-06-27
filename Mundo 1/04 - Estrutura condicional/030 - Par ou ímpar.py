"""Crie um programa que leia um número inteiro e mostre na tela se ele
é PAR ou ÍMPAR."""
from utils import cores
numero = int(input(f"{cores.ROXO}Digite um número qualquer: {cores.RESET}"))

if numero % 2 == 0:
  print(f"O número {numero} é {cores.AZUL}ímpar")

else:
  print(f"O número {numero} é {cores.AZUL}par")