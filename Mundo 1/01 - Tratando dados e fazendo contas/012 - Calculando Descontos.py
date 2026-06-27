"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
com 5% de desconto."""

produto = float(input("Qual o preço do produto? R$"))

desconto = produto - (produto * 0.05)

print(f"O produto que custa R${produto:.2f} com 5% descoto custará R${desconto:.2f}")