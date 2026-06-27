"""Crie um programa que leia um número Real qualquer pelo teclado e mostre
na tela a sua porção Inteira"""
import math

numero = float(input("Digite um número flutuante: "))

print(f"O número digitado foi {numero} e sua porçao inteira é {math.trunc(numero)}")
