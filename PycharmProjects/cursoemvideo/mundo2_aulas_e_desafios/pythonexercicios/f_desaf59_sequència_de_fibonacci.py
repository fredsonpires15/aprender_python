""" Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência
 de Fibonacci. Exemplo:  0 – 1 – 1 – 2 – 3 – 5 – 8 """
# depois tentar fazer desta forma
"""termo = int(input("1º termo:"))
n = int(input("nº de sequência:"))
c = 1
while c <= n:
    sfb = (pow(1 + 5 ** 1 / 2, c) / 2 - pow(1 - 5 ** 1 / 2, c) / 2) / 5 ** 1/2
    c += 1
print("{}".format(sfb), end=" ->")"""

#  a forma mais lógica de fazer sem um formúla

print("~" * 22)
print("SEQUÊNCIA DE FIBONACCI")
print("~" * 22)

n = int(input("Quantos elementos quer mostrar? "))
f1 = 0
f2 = 1
print("{} -> {}".format(f1, f2), end=" ")
cont = 3
while cont <= n:
    f3 = f1 + f2
    print(" -> {}".format(f3), end=" ")
    cont += 1
    f1 = f2
    f2 = f3
print(" -> FIM!!")