"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
alugado a quantidade de dias pelos quais ele foi alugado. Calcule o preço
a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado"""

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km percorridos? "))

valor_dia = dias * 60
valor_km = km * 0.15

total = valor_dia + valor_km

print(f"O total a pagar é R${total:.2f}")