"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
 e quantas já são maiores"""
import datetime

ano_atual = datetime.datetime.now().year

maioridade = 0
menoridade = 0

for indice in range(1, 8):

  ano_de_nascimento = int(input(f"Digite o ano de nascimento da {indice}° pessoa: "))
  idade = ano_atual - ano_de_nascimento

  if idade < 18:
    menoridade += 1

  else:
    maioridade += 1

print(f"Ao todos {maioridade} pessoas são de maioridade")
print(f"E {menoridade} pessoas são de menoridade")