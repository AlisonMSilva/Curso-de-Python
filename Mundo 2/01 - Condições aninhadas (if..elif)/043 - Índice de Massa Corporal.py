"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""

peso = float(input("Qual é o seu peso? (Kg): "))
altura = float(input("Qual é a sua altura? (m): "))

indice = peso / (altura ** 2)

print("Classificação para adultos")

if indice < 18.5:
    IMC = "ABAIXO DO PESO"

elif indice < 25:
    IMC = "PESO NORMAL"

elif indice < 30:
    IMC = "SOBREPESO"

elif indice < 35:
    IMC = "OBESIDADE GRAU I"

elif indice < 40:
    IMC = "OBESIDADE GRAU II"

else:
    IMC = "OBESIDADE GRAU III"

print(f"O seu IMC é {indice:.1f} e sua clasifiação está {IMC}")
