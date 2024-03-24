""" Faça um programa que leia um número
 qualquer e mostre o seu fatorial"""

"""from math import factorial
print("\033[1:33m<>==\033[m" * 7)
num = int(input("Indica um valor para \n calcular Fatorial:"))
while num != 0:
    fact = factorial(num)
    print(fact)"""

num = int(input("\033[35:1mDigite um valor para \n Calcular seu Fatorial:"))
n = num
fact = 1
if n >= 0:
    print("\033[37:1mCalculando \033[34m{}! = \033[m".format(num), end=" ")
else:
    print("Valor negativo!!")
while n > 0:
    print("\033[33m {}".format(n), end=" ")
    print("\033[39:1mx" if n > 1 else "\033[39:1m = ", end=" ")
    fact *= n
    n -= 1
if n >= 0:
    print("\033[33m{}".format(fact))
