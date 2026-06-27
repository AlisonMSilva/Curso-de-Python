"""A Confederação Nacional de Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER"""
import datetime

data_de_nascimento = int(input("Data de nascimento: "))

ano_atual = datetime.datetime.now().year

idade = ano_atual - data_de_nascimento

if idade <= 9:
  classificacao = "MERIM"

elif idade <= 14:
  classificacao = "INFANTIL"

elif idade <= 19:
  classificacao = "JÚNIOR"

elif idade <= 25:
  classificacao = "SÊNIOR"

elif idade > 25 and idade <= 50:
  classificacao = "MASTER"

print(
  f"O atleta têm {idade} anos de idade\n"
  f"Sua classificação é {classificacao}"
)

