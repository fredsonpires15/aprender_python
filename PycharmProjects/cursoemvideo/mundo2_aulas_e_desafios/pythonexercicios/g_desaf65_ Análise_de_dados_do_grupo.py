"""Crie um programa que leia a idade e o sexo de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

from datetime import date
from time import sleep

contpessoa = 0
conthomem = 0
contmulher = conttodos = 0
while True:
    nascpessoa = int(input("Data de nascimento:"))
    anoatual = date.today().year
    idade = anoatual - nascpessoa
    if idade >= 18:
        contpessoa += 1
    sexo = " "
    while sexo not in "Mm/Ff":
        sexo = str(input("Sexo [M/F]")).upper().strip()
        conttodos += 1
        if sexo == "M":
            conthomem += 1
        elif sexo == "F":
            if idade < 20:
                contmulher += 1
    print("_-" * 15)
    op = " "
    while op not in "SN":
        op = str(input("Quer continuar? [S/N]")).upper().strip()
    print("_-" * 15)
    if op == "N":
        break
print("A analisar os dados estátisticos...")
sleep(1)
print("=" * 30)
print(f"Com os dados obtidos constatamos que:\n"
      f"a) - temos {contpessoa} com mais de 18 anos\n"
      f"b) - Num total de {conttodos} pessoa(s) {conthomem} são homem\n"
      f"C) - E {contmulher} são mulher(es) tem menos de 20 anos.")
