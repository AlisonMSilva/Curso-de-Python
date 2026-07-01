"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
Aula Anterior
Voltar para Módulo
"""
import os

print("\033[1;36mCalculadora\033[m")

n1 = input("Digite o 1° número: ")
n2 = input("Digite o 2° número: ")

# Validação númerica
while not n1.isnumeric():
   n1 = input("Dado inválido, digite um número válido: ")

while not n2.isnumeric():
   n2 = input("Dado inválido, digite um número válido: ")

# Converção
n1 = float(n1)
n2 = float(n2)

op = 0

while op != 5:
    os.system("clear")

    print(
        "\n[ 1 ] somar"
        "\n[ 2 ] multiplicar"
        "\n[ 3 ] maior"
        "\n[ 4 ] novos números"
        "\n[ 5 ] sair do programa"
    )

    op = input(">>>> \033[32mEscolha uma das operações\033[m: ")

    while not op.isdigit():
      op = input("Digite apenas números: ")
    op = int(op)

    while op not in [1, 2, 3, 4, 5]:
        op = input("Escolha uma opção válida: ")
        while not op.isdigit():
          op = input("Digite apenas números: ")
        op = int(op)

    if op == 1:
        os.system("clear")
        print(f"A soma entre {n1} + {n2} é igual a {n1 + n2}")
        input("\033[32mENTER para continuar...\033[m")

    elif op == 2:
        os.system("clear")
        print(f"O número {n1} x {n2} é igual a {n1 * n2}")
        input("\033[32mENTER para continuar...\033[m")

    elif op == 3:
        os.system("clear")
        if n1 > n2:
            print(f"O maior número digitado é {n1}")
        elif n2 > n1:
            print(f"O maior número digitado é {n2}")
        else:
            print("Os dois números são iguais.")
        input("\033[32mENTER para continuar...\033[m")

    elif op == 4:
        os.system("clear")

        n1 = input("Digite o 1° número: ")
        while not n1.isnumeric():
            n1 = input("Dado inválido, digite um número válido: ")
        n1 = float(n1)

        n2 = input("Digite o 2° número: ")
        while not n2.isnumeric():
            n2 = input("Dado inválido, digite um número válido: ")
        n2 = float(n2)

        input("\033[32mENTER para continuar...\033[m")

print("\033[31mPrograma encerrado!\033[m")