"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for"""

numero = int(input("Digite um número para ver sua tabúada: "))

for c in range(0, 10):
  c += 1
  resultado = c * numero

  print(f"{numero} X {c} = {resultado}")
  