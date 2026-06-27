"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""

n1 = float(input("Qual foi sua 1° nota? "))
n2 = float(input("Qual foi sua 2° nota? "))

media = (n1 + n2) / 2

if media < 5:
  print(f"Sua média foi {media} pontos você está \033[31mREPROVADO!\033[m")
  print(f"Infelizmente faltou {7 - media} para suar aprovação")

elif media < 6.9:
  print(f"Sua média foi {media} pontos você está em \033[33mRECUPERACÃO!\033[m")
  print(f"Você precisará de {7 - media} pontos a mais para ser APROVADO")

elif media >= 7:
  print(f"Sua média foi {media} pontos você está \033[32mAPROVADO!\033[m")
