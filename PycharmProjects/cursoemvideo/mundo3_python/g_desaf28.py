""" Exercício Python 100: Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior. """

from random import randint
from time import sleep



def sorteiar(lista):
    print('Os valores sorteados são: ' ,end='')
    for i in range(0,6):
        num = randint(1,10)
        lista.append(num)
        print(f'{num}',end=' ')
        sleep(0.3)
    print(': Pronto!!')   

def somapar(lista):
    soma = 0
    for valor in lista:      
       if valor % 2 == 0:
           listapar.append(valor)
           soma+= valor 
    print(f'Somando os valores par {listapar}, temos {soma}')

lista = []
listapar = list()
sorteiar(lista)
somapar(lista)