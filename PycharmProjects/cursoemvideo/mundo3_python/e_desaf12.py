""" Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:   
 A) Quantas pessoas foram cadastradas. 
 B) Uma listagem com as pessoas mais pesadas. 
 C) Uma listagem com as pessoas mais leves. """

lista = []
listar_tudo = []
maior = menor = 0
contpessoas = 0
while True:
    lista.append(str(input('Nome:')))
    lista.append(float(input('Peso:')))
    if len(listar_tudo) == 0:
        maior = menor = lista[1]
    else:
        if lista[1]> maior:
            maior = lista[1]
        if lista[1]<menor:
            menor = lista[1]

    listar_tudo.append(lista[:])
    lista.clear()
    
    contpessoas += 1
    sair = str(input('Quer continuar? [Ss/Nn]: '))
    if sair.upper() == 'N':
        break   
  
print(f'Foram cadastradas {contpessoas} pessoas neste processo')
print(f'O maior peso foi de {maior}Kg. Peso de ', end=' ')
for pessoa in listar_tudo:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end=' ')
print()
print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end=' ')
for pessoa in listar_tudo:
    if pessoa[1]==menor:
        print(f'{pessoa[0]}', end=' ')

