"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número 
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

import random

computador = random.randint(0, 10)
print("\033[32m" \
"🤖 Sou seu computador..." \
"Acabei de pensar em um número entre 0 e 10:\033[m")

jogador = input("Digite um número entre 0 e 10: ")

# 1° Válidação
while not jogador.isdigit() or not 0 <= int(jogador) <= 10:
    jogador = input("Entrada inválida! Digite um número entre 0 e 10: ")

jogador = int(jogador)
tentativas = 1

while computador != jogador:
  print("Tente novamente: ")
  tentativas += 1

  if computador > jogador:
    jogador = input("Mais... ")
  elif computador < jogador:
    jogador = input("Menos... ")

  # 2° Válidação
  while not jogador.isdigit() or not 0 <= int(jogador) <= 10:
      jogador = input("Entrada inválida! Digite um número entre 0 e 10: ")

  jogador = int(jogador)

print(f"Parabéns, \033[32mvocê acertou\033[m com {tentativas} tentativas!🎉")