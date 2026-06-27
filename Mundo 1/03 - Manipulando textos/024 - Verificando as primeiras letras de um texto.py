""" Crie um programa que leia o nome de uma cidade diga se ela começa ou não 
com o nome “SANTO”."""
cidade = input("Em que cidade você nasce? ")
cidade_split = cidade.split()

print("Santo" in cidade_split[0].title())