"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
 quantos dólares ela pode comprar"""
import requests

carteira = float(input("Quantos R$ você possui na carteira R$"))

api = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")

dados = api.json()

cotacao = float(dados["USDBRL"]["bid"])

compra = carteira / cotacao

print(f"Com R${carteira} você pode comprar US{compra:.2f}")

# API Utilizada
# https://docs.awesomeapi.com.br/api-de-moedas?utm_source=chatgpt.com