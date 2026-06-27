"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na
 tela a sua porção Inteira"""

cel = float(input("Digite um valor em °C: "))

# multiplica por 9, depois divide por 5 e então soma + 32
fah = (cel * 9 / 5) + 32

print(f"A temperatura {cel}°C corresponde á {fah}°F")