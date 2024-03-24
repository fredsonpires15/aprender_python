"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado. """


from random import  randint
from time import sleep
from operator import itemgetter


ranking = dict()

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6), 
        'jogador3': randint(1,6), 
        'jogador4': randint(1,6) }

for jogador, resultado in jogo.items():
    print(f'O {jogador} tirou {resultado} no dado.')
    sleep(1)

print()
print('==================================')
print('    ==RANIKG DOS JOGADORES==   ')
sleep(3)
ranking = sorted(jogo.items(), key=itemgetter(1) ,  reverse=True)

for pos, r in enumerate(ranking):
    print(f'   {pos+1}º lugar: {r[0]} com {r[1]}')
    sleep(1)

print()
print()
