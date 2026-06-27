"""Faça um programa que calcule a soma entre todos os números que são múltiplos 
de três e que se encontram no intervalo de 1 até 500"""

print("Verificando os múltiplos de 3")

# Entradas de dados
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

# Validação do intervalo
if inicio > fim:
    print("Erro: o número inicial deve ser menor ou igual ao número final.")

else:
    # Variáveis de controle
    soma = 0
    contador = 0
    maior = None

    # Processamento
    for multiplo in range(inicio, fim + 1):
        if multiplo % 3 == 0:
            soma += multiplo
            contador += 1
            maior = multiplo

    # Resultado
    if contador == 0:
        print("Não existem múltiplos de 3 nesse intervalo.")
    else:
        print(f"A soma entre todos os {contador} múltiplos de 3 é {soma}")
        print(f"O maior múltiplo de 3 foi o número {maior}")