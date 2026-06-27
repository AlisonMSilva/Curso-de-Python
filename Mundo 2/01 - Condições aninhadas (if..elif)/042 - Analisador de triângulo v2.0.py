"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes"""

print("-=" * 30)
print("Analisador de triângulos")
print("-=" * 30)

A = float(input("Digite o 1° segmento: "))
B = float(input("Digite o 2° segmento: "))
C = float(input("Digite o 3° segmento: "))

print("-=" * 30)
print("Analisador de triângulos")
print("-=" * 30)

A = float(input("Digite o 1° segmento: "))
B = float(input("Digite o 2° segmento: "))
C = float(input("Digite o 3° segmento: "))

if A < B + C and B < A + C and C < A + B:

    if A == B == C:
        triangulo = "EQUILÁTERO"

    elif A == B or A == C or B == C:
        triangulo = "ISÓSCELES"

    else:
        triangulo = "ESCALENO"

    print(f"Com base nos segmentos, o triângulo é {triangulo}")

else:
    print("Não é possível formar um triângulo com base nos segmentos.")