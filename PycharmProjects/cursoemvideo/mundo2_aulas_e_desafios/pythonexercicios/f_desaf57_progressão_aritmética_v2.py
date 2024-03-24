""" Refaça o DESAFIO 47, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while."""

termo = int(input("Primeiro termo:"))
razao = int(input("Razão:"))
c = 1

while c < 11:
    pA = termo + (c - 1) * razao

    print("{}". format(pA), end="-> ")
    c += 1
print("Acabou!!")
