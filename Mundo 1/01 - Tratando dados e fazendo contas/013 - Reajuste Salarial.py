"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento"""

salario = float(input("Qual é o sálario do funcionário? R$"))

reajuste = salario + (salario * 0.15)

print(f"O funcionário que recebe R${salario:.2f} passará a receber R${reajuste:.2f} com os 15% de reajuste")