""" Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares. """

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o primeiro número: '))
num3 = int(input('Digite o primeiro número: '))
num4 = int(input('Digite o primeiro número: '))

tupla = (num1, num2, num3, num4)
print(f'Os números digitados são: {tupla}')
print(f' O número 9 apareceu {tupla.count(9)} veze(s)')
if 3 in tupla:
    print(f'O número 3 está na {tupla.index(3)+1} ª posição')
else:
    print('Não existe número 3 na tupla')
    
print('Os números pares foram', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(f'{i}',end=' ')