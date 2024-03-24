"""Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date

data = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input("Ano de nascimento da {}ª pessoa?".format(c)))
    idade = data - nasc
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print("Contudo tivemos {} pessoas menores de idade".format(menor))
print("E também tivemos {} pessoas são maiores de idade".format(maior))

