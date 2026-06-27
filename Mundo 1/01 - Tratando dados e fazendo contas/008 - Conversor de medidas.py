"""Escreva um programa que leia um valor em metros e o exiba convertido em 
centímetros e milímetros."""
metros = float(input("Digite uma distância em metro: "))

cm = metros * 100
mm = metros * 1000
polegagas = metros * 39.38

print(f"{metros} metros equivale a")
print(f"{cm} centímetros")
print(f"{mm} milímetros")
print(f"{polegagas} polegadas")