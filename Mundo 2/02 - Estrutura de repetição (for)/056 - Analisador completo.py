""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do 
homem mais velho e quantas mulheres têm menos de 20 anos."""
import math

idade_acumulador = 0

nome_mais_velho = ""
maior_idade = 0

mulheres_menor = 0

for indice in range (1, 4 + 1):
  print(f"---- {indice}° Pessoa ----")
  nome = input(f"{indice}° Pessoa: ")
  idade = int(input("Idade: "))
  sexo = input("Sexo [M/F]: ").upper()

  # Acumula as idades
  idade_acumulador += idade

  if sexo == "M" and idade > maior_idade:
    nome_mais_velho = nome
    maior_idade = idade

  if sexo == "F" and idade < 20:
    mulheres_menor += 1

media_idade = idade_acumulador / 4

print(f"A média de idade do grupo é de {math.trunc(idade)} anos")
print(f"O homem mais velho possui {maior_idade} e se chama {nome_mais_velho}")
print(f"Ao todos {mulheres_menor} mulheres possuem menos de 20 anos")