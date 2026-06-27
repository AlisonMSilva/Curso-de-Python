"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
primitivo e todas as informações possíveis sobre ele."""

frase = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(frase)}")
print("Só têm espaços? ", frase.isspace())
print("É um número? ", frase.isnumeric())
print("É alfabético? ", frase.isalpha())
print("É alphanúmerico? ", frase.isalnum())
print("Está tudo em maiúsculas?", frase.isupper())
print("Está tudo em menúsculas? ", frase.islower())
print("Está capitalizada? ", frase.istitle())