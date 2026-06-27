"""Exercício Python 059: Crie um programa que leia dois valores e
mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""
# bibliotecas
import os

# cores
verde = "\033[32m"
reset = "\033[m"

# valores
print("\033[34mCalculadora\033[m")
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

escolha = ""

while escolha != 6:
  print("\033[34mEscolha uma das operação que você deseja realizar\033[m")
  print("[ 1 ] Somar")
  print("[ 2 ] Subtrair")
  print("[ 3 ] Multiplicar")
  print("[ 4 ] Dividir")
  print("[ 5 ] Alterar números")
  print("[ 6 ] Sair")

  escolha = int(input("Qual a operação desejada: "))

  if escolha == 1:
    os.system("clear")
    print(f"{verde}O soma entre {n1} + {n2} é {n1 + n2}{reset}")
    input("\nPressione ENTER para continuar...")

  elif escolha == 2:
    os.system("clear")
    print(f"{verde}A subtração entre {n1} - {n2} é {n1 - n2}{reset}")
    input("\nPressione ENTER para continuar...")

  elif escolha == 3:
    os.system("clear")
    print(f"{verde}A multiplicação de {n1} X {n2} é igual a {n1 * n2}{reset}")
    input("\nPressione ENTER para continuar...")

  elif escolha == 4:
    os.system("clear")
    print(f"{verde}A subtração entre {n1} % {n2} é {n1 / n2}{reset}")
    input("\nPressione ENTER para continuar...")

  elif escolha == 5:
    os.system("clear")
    n1 = int(input("Qual o novo valor do 1° número: "))
    n2 = int(input("Qual o novo valor do 2° número: "))
    print(f"Valores atualizados para {verde}{n1}{reset} e {verde}{n2}{reset}")
    input("\nPressione ENTER para continuar...")

os.system("clear")
print("\033[31mPrograma finalizado!\033[m")