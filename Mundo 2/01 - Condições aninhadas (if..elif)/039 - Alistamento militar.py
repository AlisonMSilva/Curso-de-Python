"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

import datetime
ano_de_nascimento = int(input("Digite o ano em que você nasceu: "))

# Captura o ano atual
ano_atual = datetime.datetime.now().year

# Calcula a idade com base no ano
idade_atual = ano_atual - ano_de_nascimento

print(f"Quem nasceu em {ano_de_nascimento} têm {idade_atual} em {ano_atual}")

if idade_atual < 18:
  print(f"Faltam {18 - idade_atual} anos para você se alistar")
  print(f"Seu alistamento será em {ano_de_nascimento + 18}")

elif idade_atual > 18:
  print(f"Você já deveria ter se alistado á {idade_atual - 18} anos")
  print(f"Seu alistamento foi em {ano_de_nascimento + 18}")

elif idade_atual == 18:
  print("Você deve se apresentar ainda este ANO!")