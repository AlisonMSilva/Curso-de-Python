"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
correto."""

sexo = input("Informe seu sexo: [M/F]: ").upper()

# Validação de dados
while sexo not in "MF":
 print("Dados inválidos: ")
 sexo = input("Por favor, informe seu sexo: [M/F]: ").upper()

# Atualização
if sexo == "M":
 sexo = "Masculino"
else:
 sexo = "Feminino"

print(f"Sexo {sexo} registrado com sucesso")