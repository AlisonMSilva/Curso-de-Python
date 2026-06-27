"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes 
aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição 
ela aparece a última vez"""

frase = input("Digite uma frase: ")
frase_lower = frase.lower()

print(f"A letra 'a' apareceu {frase_lower.count('a')}")
print(f"A primeira ocorrencia aconteceu na posição {frase_lower.find("a") + 1}")
print(f"A ultima ocorrencia aconteceu na posição {frase_lower.rfind("a") + 1}")