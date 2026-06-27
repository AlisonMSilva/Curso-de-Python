#  Crie um programa que faça o computador jogar Jokenpô com você.
import random, time

print("\033[1;32mSuas opções\033[m")
print("[ 1 ] PEDRA")
print("[ 2 ] PAPEL")
print("[ 3 ] TESOURA")

escolhas = ["PEDRA", "PAPEL", "TESOURA"]

jogador = int(input("Qual é sua jogada: "))
pc = random.randint(1, 3)
resultado = None

# EMPATE
if jogador == pc:
  resultado == "EMPATE"

# VITÓRIA
elif (
  # Casos de vitória
  (jogador == 1 and pc == 3) or 
  (jogador == 2 and pc == 1) or 
  (jogador == 3 and pc == 2)
):
  resultado = "\033[32mJOGADOR VENCEU 🎉\033[m"

else:
  resultado = "\033[31mCOMPUTADOR VENCEU\033[m"

print("Jo")
time.sleep(1)
print("Ken")
time.sleep(1)
print("Pô")
time.sleep(1)

print(15 * "\033[33m-=\033[m")
print(f"Jogador jogou {escolhas[jogador - 1]}")
print(f"Computador jogou {escolhas[pc - 1]}")
print(15 * "\033[33m-=\033[m")

print(f"Resultado da partida {resultado}")