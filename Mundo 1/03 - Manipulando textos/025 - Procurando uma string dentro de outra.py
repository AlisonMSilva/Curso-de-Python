"""Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” 
no nome."""

nome = input("Qual é o seu nome completo: ")


print(f"Seu nome possui Silva? {"Silva" in nome.title().strip()}")