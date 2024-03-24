"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
totpreco = 0
totproduto = contpreco = menor = 0
barato = " "
while True:
    prod = str(input("Nome do produto:"))
    preco = float(input("Preço:"))
    contpreco += 1
    totpreco += preco
    if preco >= 1000:
        totproduto += 1

    if contpreco == 1:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    print("=»" * 20)
    op = " "
    while op not in "SN":
        op = str(input("Quer continuar? [S/N]")).upper().strip()
    print("_" * 20)
    if op == "N":
        break
print("___________Estatística em produtos______________")
print(f"Total de conta:_______________________ {totpreco:.2f}€")
print(f"Nesta compra {totproduto} custa mais de_____________1000€")
print(f"O produto mais barato é {barato} que custa_______ {menor}£")
print()
print(f"{' FIM DO PROGRAMA!! ':_^50}")
