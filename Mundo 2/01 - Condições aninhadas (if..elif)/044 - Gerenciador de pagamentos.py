"""labore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros"""

# variáveis de cores e estilos
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
bold = "\033[1m"
reset = "\033[m"


print(f"{azul}========== LOJAS GUANABARA =========={reset}")

valor_da_compra = float(input(f"{bold}Informe o preço das compras: R${reset}"))

print(f"{azul}FORMAS DE PAGAMENTO{reset}")
print("[ 1 ] À vista dinheiro/pix")
print("[ 2 ] À vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")

pagamento = int(input(f"{amarelo}Qual a opção: {reset}"))

if pagamento == 1:
    total = valor_da_compra * 0.90

elif pagamento == 2:
    total = valor_da_compra * 0.95

elif pagamento == 3:
    total = valor_da_compra

elif pagamento == 4:
    parcelas = int(input("Em quantas vezes você quer parcelar? "))

    if parcelas < 3:
      print(f"{vermelho}Esse valor de parcelamento é INVÁLIDO{reset}")
      exit()

    else:
      total = valor_da_compra * 1.20
      print(
          f"Sua compra será parcelada em {parcelas}x "
          f"de {verde}R${total / parcelas:.2f}{reset}"
          )

else:
    print("Opção inválida!")
    total = valor_da_compra

print(f"O valor final da sua compra é de {verde}R${total:.2f}{reset}.")