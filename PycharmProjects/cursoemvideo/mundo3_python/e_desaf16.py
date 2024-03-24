""" Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta """


from random import randint
from time import sleep

lista_de_sorteo = []
jogos = []
cont = 0 
tot = 1
quanto = int(input('quantos jogos você quer eu sorteie? '))
while tot <= quanto:
    cont = 0
    while True:
        sorteo = randint(1,60)
        if sorteo not in lista_de_sorteo:
            lista_de_sorteo.append(sorteo) 
            cont += 1
        if cont >= 6:
            break   
    lista_de_sorteo.sort()
    jogos.append(lista_de_sorteo[:])
    lista_de_sorteo.clear()
    tot +=1
print()
print()
for ind, sorteado in enumerate(jogos):  
    print(f'jogo {ind+1:^2}: {sorteado}')
    sleep(1)
print()
print()
print('-='*5,'BOA SORTE!!','-='*5)
print()
print()
print()
