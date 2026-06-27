"""O mesmo professor do desafio 19 quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
mostre a ordem sorteada."""
import random

aluno_1 = input("Primeiro  Aluno: ")
aluno_2 = input("Segundo   Aluno: ")
aluno_3 = input("Terceiro  Aluno: ")
aluno_4 = input("Quarto    Aluno: ")

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

lista_atualizada = random.shuffle(alunos)

print("\nOrdem de apresentação:")
print(f"1° {alunos[0]}")
print(f"2° {alunos[1]}")
print(f"3° {alunos[2]}")
print(f"4° {alunos[3]}")