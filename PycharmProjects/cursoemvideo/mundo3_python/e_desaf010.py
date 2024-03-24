""" 
Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os ves
pares e os ves ímpares digitados, respectivamente. Ao final, mostre
 o conteúdo das três listas geradas. """

lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um valor: ')))

    sair = str(input('Quer continuar? [S/N]: ')) 
    if sair in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)

print(f'Lista com todos os números: {lista}')   
print(f'Lista com números pares: {lista_par}')
print(f'Lista com números impares: {lista_impar}')