# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
from utils import cores

ano = int(input("Digite o ano, ou 0 para o ano atual: "))

if ano == 0: # Atualiza o valor atual e segue 
  ano = datetime.datetime.now().year

if ano % 400 == 0 or ano % 100 != 0 and ano % 4 == 0:
  print(
  f"O ano de {cores.AZUL}{ano}{cores.RESET} "
  f"{cores.VERDE}é Bissexto{cores.RESET}"
  )

else:
  print(
  f"O ano de {cores.AZUL}{ano}{cores.RESET}{cores.VERMELHO} "
  f"não é Bissexto{cores.RESET}"
  )