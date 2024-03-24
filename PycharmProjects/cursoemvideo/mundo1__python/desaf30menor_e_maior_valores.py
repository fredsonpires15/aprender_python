n1 = int(input("primeiro número:"))
n2 = int(input("Segundo número:"))
n3 = int(input("Terceiro número:"))
# verificando quem é menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print("O menor valor é {} ".format(menor))
#  verificando qual é o maior valor
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print("O maior valor é {}".format(maior))