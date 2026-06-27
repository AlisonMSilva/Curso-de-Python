"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do 
seno, cosseno e tangente desse ângulo"""
import math

angulo = float(input("Digite o ângulo que você deseja: "))

# precisamos converter para radiano
radiano = math.radians(angulo)

print(f"O ângulo de {angulo} possui o seno de {math.sin(radiano):.2f}")
print(f"O ângulo de {angulo} possui o cosseno de {math.cos(radiano):.2f}")
print(f"O ângulo de {angulo} possui a tangente de {math.tan(radiano):.2f}")
