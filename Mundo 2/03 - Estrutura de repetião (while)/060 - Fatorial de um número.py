"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120"""
import math

print("\033[1;35mFatorial de um número\033[m")

numero = int(input("Digite um número inteiro: "))
contador = numero

while contador > 0:
  #  O contador é exibido enquanto decresce
  print(f"{contador}", end="")
  # 'x' sempre será exibidp enquanto contador for maior que 0
  print(" x"if contador > 1 else " =", end=" ")

  # A cada loop o contador diminui
  contador -= 1


print(f"{math.factorial(numero)}")