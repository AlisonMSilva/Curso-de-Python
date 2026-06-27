"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma 
casa. 
1. Pergunte o valor da casa
2. O salário do comprador
3. Em quantos anos ele vai pagar
A prestação mensal não pode exceder 30% do salário ou então o empréstimo 
será negado."""

valor_da_casa = float(input("Valor da casa R$"))
salario_comprador = float(input("Qual o salário do comprador R$"))
tempo_financiamento = int(input("Em quantos anos pretende quitar: "))

# Converte os anos em meses
quantidade_de_mese = tempo_financiamento * 12

# Calcula o valor das parcelas mensais
valor_prestacao = valor_da_casa / quantidade_de_mese

# Limite que não pode ser execido
limite_permitido = salario_comprador * 0.30

print(
  "\n"
  f"Para pagar uma casa de {valor_da_casa:.2f}R$ em {tempo_financiamento} anos"
  f" Será necessário {valor_prestacao:.2f}R$ mensal para quitar"
)

if valor_prestacao > limite_permitido:
  print("Empéstimo \033[31mNEGADO!\033[m")

else:
  print("Empréstimo \033[32mAPROVADO!\033[m")
