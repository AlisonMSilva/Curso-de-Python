"""Escreva um programa que faça o computador “pensar” em um número inteiro entre
0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo 
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""
import random, time
from utils import cores

print(f"{cores.AMARELO}-={cores.RESET}" * 30)
print(f"{cores.AZUL}Vou pensar em um número entre 1 e 5. Tente adivinhar...{cores.RESET}")
print("-=" * 30)

numero_pensado = random.randint(1, 5)
numero_jogador = int(input("Em que número estou pensando? "))

print(f"{cores.ROXO}PENSANDO...{cores.RESET}")
time.sleep(3)

if numero_pensado == numero_jogador:
  print(f"{cores.VERDE}Parabéns 🥳, você acertou 🎉🎉{cores.RESET}")

else:
  print(f"{cores.VERMELHO}Ganhei! eu pensei no número {numero_pensado} e não no {numero_jogador}!{cores.RESET}")