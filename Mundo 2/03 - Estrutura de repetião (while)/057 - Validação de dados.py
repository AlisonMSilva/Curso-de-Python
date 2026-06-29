"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor 
correto."""

sexo = input("Informe seu sexo [M / F]: ").upper()

while sexo not in "M F":
  sexo = input("Dados inválidos, por favor informe seu sexo [M / F]: ").upper()

if sexo == "M":
  sexo = "Masculino"
else:
  sexo = "Feminino"

print(f"Sexo {sexo} registrado com sucesso!")
