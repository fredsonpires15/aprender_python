""" Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 
e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta. """


matriz = [[0,0,0], [0,0,0], [0,0,0]]

for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = int(input(f'Digita um valor para [{c}, {i}]: '))
print()
print()
print()
for c in range(0,3):
    for i in range(0,3):
        print(f'{matriz[c][i]:^4}', end=' ')
    print()
print()
print()
print()
print()
   
