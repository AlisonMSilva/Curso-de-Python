"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número 
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer"""
import random

print("===== \033[35mAdivinhe em qual número estou pensando\033[m =====")

numero = random.randint(0, 10)
palpite = ""
tentativas = 1


while palpite != numero:
    tentativas += 1

    entrada = input("Digite seu palpite: ")

    if not entrada.isdigit():
        print("Digite apenas números!")
        continue

    palpite = int(entrada)

    if palpite < 0 or palpite > 10:
        print("O palpite deve ser entre 0 e 10!")
        continue

    if palpite > numero:
        print("Menos, tente novamente...")
    elif palpite < numero:
        print("Mais, tente novamente...")

print(f"Parabéns 🥳🎉, você acertou com {tentativas} tentativas")