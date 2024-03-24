""" Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente """
from time import sleep
lista = []
lista2 = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota1: ')))
    lista.append(float(input('Nota2: ')))
    lista2.append(lista[:])
    lista.clear()
    sair = str(input('Quer continuar, [Ss/Nn]: '))

    if sair.upper() == 'N':
        break
print()
print()
print()
print('_'*26)
print(f'{"Num":<4}    {"Nome":<10}{"Média":>8}')

for ind, d in enumerate(lista2):
    print('_'*26)
    print(f'{ind:<4}    {d[0]:<10}{(d[1]+d[2])/2:>8.1f}')
    sleep(2)
while True:
    opc = int(input('Quer ver as notas de qual aluno, nº? (digite 999 para sair): '))
    if opc == 999:
        break
    
    if opc <= len(lista2)-1:
        print(f'As notas de {lista2[opc][0]} são n1={lista2[opc][1]} e n2={lista2[opc][2]}')

    