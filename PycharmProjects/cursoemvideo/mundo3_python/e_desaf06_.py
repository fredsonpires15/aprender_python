""" Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista. """

""" valores = list()
for i in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(f'lista de valores:{valores}')
print(f'O maior valor é {max(valores)} está na posição {valores.index(max(valores))}')
print(f'O maior valor é {min(valores)} está na posição {valores.index(min(valores))}') """

valores = list()
menor = 0 
maior = 0
for i in range(0,5):
    valores.append(int(input('Digite um valor: ')))

    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i]> maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]
print(f'Você digitou:{valores}')
print(f'O maior valor digitado foi {maior} nas posições', end=' -> ')

for pos, val in enumerate(valores):
    if val == maior:
        print(f'{pos+1}...',end=' ')
print(' ')

print(f'O maior valor digitado foi {menor} nas posições', end=' -> ')
for pos, val in enumerate(valores):
    if  val == menor:
        print(f'{pos+1}...', end=' ')