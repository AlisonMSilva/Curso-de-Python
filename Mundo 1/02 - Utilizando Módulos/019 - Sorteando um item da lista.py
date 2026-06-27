"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
o nome do escolhido."""
import random

aluno_1 = input("Primeiro  Aluno: ")
aluno_2 = input("Segundo   Aluno: ")
aluno_3 = input("Terceiro  Aluno: ")
aluno_4 = input("Quarto    Aluno: ")

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

print(f"O Aluno escolhido é {random.choice(alunos)}")