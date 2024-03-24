"""Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""


nome = str(input('Nome: '))
media = float(input(f'Média  de {nome} : '))    

if media < 10:
    situacao = 'Reprovado'
elif media >= 10:
    situacao = 'Aprovado'
dicionario = {'nome': f' - Nome é igual a {nome}', 
              'media': f' - A média é igual a {media}',
              'situacao': f' - Aluno {situacao}'
              }

print()
print()

for v in dicionario.values():
    print(v)

print()
print()
