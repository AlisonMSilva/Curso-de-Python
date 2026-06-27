"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente."""

nome_completo = input("Digite o seu nome completo: ")
nome_splitado = nome_completo.split()

print("Muito prazer em te conhecer!")
print(f"O seu primeiro nome é {nome_splitado[0]}")
print(f"O seu último nome é {nome_splitado[-1]}")