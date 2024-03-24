""" Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
 A) A soma de todos os valores pares digitados.
 B) A soma dos valores da terceira coluna. 
 C) O maior valor da segunda linha. """


matriz = [[0,0,0], [0,0,0], [0,0,0]]

for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = int(input(f'Digita um valor para [{c}, {i}]: '))
print()
print()
print('A matriz é: ')
print()
somar = 0
somarterc = 0
maiorseg = 0
cont = 0
for c in range(0,3):
    for i in range(0,3):
        print(f'{matriz[c][i]:^4}', end=' ')
        if  matriz[c][i]%2 == 0:
            somar+= matriz[c][i]
            cont +=1
    somarterc += matriz[c][i]
    print()

for c in range(0,3):
    if c==0:
        maiorseg = matriz[1][i]
    elif matriz[1][i] > maiorseg:
        maiorseg = maiorseg[1][i] 


print()
print()
print(f'Foram digitados {cont} valores pares e a soma é {somar}')
print(f'A soma da terceira coluna é {somarterc}')
print(f'O maior valor da segunda linha é {maiorseg}')