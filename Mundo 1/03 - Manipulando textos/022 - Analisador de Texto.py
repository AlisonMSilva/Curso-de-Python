"""Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""
import time
nome = input("Digite o seu nome completo: ")

print("Analisando seu nome.")
time.sleep(1)

print("Analisando seu nome..")
time.sleep(1)

print("Analisando seu nome...")
time.sleep(1)

print(f"\nO seu nome em maiúsculas é {nome.strip().upper()}")
print(f"O seu nome em minúsculas é {nome.strip().lower()}")
print(f"O seu nome possui {len(nome.replace(" ", "").strip())} caracteres")
print(f"O seu primeiro nome é {nome.split()[0]}")
print(f"O seu último nome é {nome.split()[-1]}")