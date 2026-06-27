"""Escreva um programa em Python que leia um número inteiro qualquer e peça para 
o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal
e 3 para hexadecimal."""

numero = int(input("\033[35mDigite um número inteiro: \033[m"))

print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")

escolha = int(input("Escolha uma das conversões: "))

print(f"Sua opção: {escolha}")

if escolha == 1:
  mensagem = "BINÁRIO"
  base = bin(numero)[2:]

elif escolha == 2:
  mensagem = "OCTAL"
  base = oct(numero)[2:]

elif escolha == 3:
  mensagem = "HEXADECIMAL"
  base = hex(numero)[2:]

else:
    print("Opção inválida!")

print(f"{numero} Convertido para {mensagem} equivale a {base}")