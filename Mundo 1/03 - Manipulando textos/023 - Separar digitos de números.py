"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separados"""
numero = int(input("Digite um número inteiro: "))

unidade = numero % 10
dezena = (numero // 10 ) % 10
centena = (numero // 100 ) % 10
milhar = (numero // 1000 ) % 10

print(f"O número {numero} possui")
print(f"Unidades -> {unidade}")
print(f"Dezenas -> {dezena}")
print(f"Centenas -> {centena}")
print(f"Milhar -> {milhar}")