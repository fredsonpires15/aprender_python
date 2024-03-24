""" Crie um programa que vai gerar cinco números aleatórios
 e colocar em uma tupla. Depois disso, mostre a listagem de 
 números gerados e também indique o menor e o maior valor que estão na tupla. """

import random
lista = []
for num in range(5):
    num_aleatorio = random.randint(0,5)
    lista.append(num_aleatorio)
tupla = tuple(lista)
print(tupla)
print(f'o menor é {min(tupla)}')
print(f'o maior é {max(tupla)}')