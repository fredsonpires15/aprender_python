"""um programa que lê o peso de cinco pessoas.
 No final, vai mostrar qual foi o maior e o menor peso lidos."""
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {}ª pessoa:".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
if maior == menor:
    print("São todos iguais")
else:
    print("O maior peso lido foi de {}kg".format(maior))
    print("O menor peso lido foi de {}kg".format(menor))
