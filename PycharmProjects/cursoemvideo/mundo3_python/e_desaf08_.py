""" Exercício Python 079: Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente. """

lista = []

while True:
    valores = int(input('Digite um valor:'))
    if valores in lista:
        print('Já existe este valor na lista!!')
    else:
        print('valor adicionado com sucesso!!')
        lista.append(valores)
    sair = str(input('Quer continuar? [S/N]: '))
    if sair.upper() == "N":
        break
lista.sort()   
print(f' Você digitou os valores: {lista}')
