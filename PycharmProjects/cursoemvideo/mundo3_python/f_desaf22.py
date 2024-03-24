""" Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média """

dic = dict()
lista = list()
lista_de_mulheres = list()
pessoas_cadastradas = 0
soma_idade = 0
while True:
    dic['nome'] = str(input('Nome: ')) 
    pessoas_cadastradas += 1
    while True:
        dic['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if dic['sexo'] in 'MF':
            break
    dic['idade'] = int(input('Idade: '))
    soma_idade += dic['idade']
    lista.append(dic.copy()) 
    if dic['sexo'] =='F':
        lista_de_mulheres.append(dic['nome'])

    while True:
        sair = str(input('Quer sair? [Ss/Nn]: ')).upper()
        if sair in 'SN':
            break
    if sair.upper() == 'N':
        break
media = soma_idade/pessoas_cadastradas
print(f'No total foram cadastradas {pessoas_cadastradas} pessoas')
print(f'A média da idade é de {media:.2f}') 
print(f'As cadastras são: {lista_de_mulheres}') 
print()

for p in lista:
    if p['idade'] >= media:
        print(' ')
        for k,v in p.items():
            print(f'{k}={v} ', end=" ")
        print()

print()
print()
print(lista)

