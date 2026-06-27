"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA."""

frase = input("Digite uma frase: ")

# Remove espaços e padroniza tudo em minúsculo
frase_limpa = frase.replace(" ", "").lower()

# Inverte a frase
frase_invertida = frase_limpa[::-1]

print(f"A palavra {frase} invertida é {frase_invertida}")
# Verifica se é palíndromo
if frase_limpa == frase_invertida:
    print(f"É um palíndromo")
else:
    print("Não é um palíndromo")