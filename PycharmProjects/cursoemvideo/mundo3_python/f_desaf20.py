""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.  """
from time import sleep
 
cadastrar =  dict()
nome = str(input('Nome do trabalhador: '))
ano_nasc = int(input('Ano de nascimento: '))
carteira_de_Trab = int(input('Carteira de trabalho (0 se não tem): '))

if carteira_de_Trab == 0:
    cadastrar = {'nom': f'Nome do trabalhador: {nome}',
                 'ano_de_nas': f'Idade do trabalhador: {2023-ano_nasc} anos',
                 'cateira_de_tra': 'Carteira de trabalho: não tem'


                         }
  
else:
    ano_de_cont = int(input('Ano de contratação: '))
    salario = float(input('Salário: '))
    cadastrar = {'nom': f'Nome do trabalhador: {nome}',
                 'ano_de_nas': f'Idade do trabalhador: {2023-ano_nasc} anos',
                 'cateira_de_tra': f'Carteira de trabalho: {carteira_de_Trab}',
                 'ano_de_conta': f'Ano de contratação: {ano_de_cont}',
                 'salar': f'Salário: {salario:.2f}€'

                        }
print('A cadastrar trabalhador. . . .')
sleep(2)  

print()
print()
print('»='*30)   
for v in cadastrar.values():
    print(v)
print('»='*30)   
print()   
print() 