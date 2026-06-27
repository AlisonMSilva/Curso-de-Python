"""Escreva um programa que pergunte o salário de um funcionário e calcule o 
valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento 
de 10%. Para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input("Qual o sálario do funcionário? "))

if salario <= 1250:
  reajuste = (salario * 15) / 100 + salario

if salario > 1250:
  reajuste = (salario * 10) / 100 + salario

print(f"Quem ganhava {salario:.2f}R$ irá ganhar {reajuste:.2f}R$")