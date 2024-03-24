"""Crie um programa que simule o funcionamento de um caixa eletrônico.
 No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

valor = int(input("valor a ser sacado:"))
total = valor
notas = 50
contnotas = 0
while True:

    if total >= notas:
        total -= notas
        contnotas += 1
    else:
        if contnotas > 0:
            print(f"Foi sacado {contnotas} notas de {notas}€")
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        contnotas = 0
        if notas == 0:
            break
