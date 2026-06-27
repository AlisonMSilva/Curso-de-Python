"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas"""

distancia = int(input("Qual a distância da viagem? "))

if distancia <= 200:
  valor_por_km = 0.50

  print(f"O preço de sua passagem será de {distancia * valor_por_km:.2f}R$")

else:
  valor_por_km = 0.45
  print(f"O preço de sua passagem será de {distancia * valor_por_km:.2f}R$")