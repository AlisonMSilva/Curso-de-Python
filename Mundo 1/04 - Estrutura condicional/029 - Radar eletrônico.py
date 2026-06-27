"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 
R$7,00 por cada Km acima do limite."""
from utils import cores
velocidade_atual = int(input("Qual a velocidade do carro atual? "))
velocidade_maxima = 80

if velocidade_atual <= velocidade_maxima:
  print(f"{cores.VERDE}Tenha um bom dia, e dirija com cuidado{cores.RESET}")

else:
  multa = (velocidade_atual - 80) * 7
  print(
    f"{cores.VERMELHO}Multado, você excedeu o limite permitido "
    f"que é {velocidade_maxima}km{cores.RESET}")
  print(
    f"{cores.AMARELO}Você deverá pagar uma "
    f"multa no valor de {multa:.2f}R$!{cores.RESET}")