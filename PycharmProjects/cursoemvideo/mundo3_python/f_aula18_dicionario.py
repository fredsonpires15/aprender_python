pessoa = {'Nome' : 'Fredson', 'Sexo': 'M', 'Idade': '22' }
print(f"O {pessoa['Nome']} tem {pessoa['Idade']} anos.")
# print(pessoa.values()) # mostrar os resultados (imagem) 
#print(pessoa.items()) # mostrar os items
#print(pessoa.keys()) # mostrar a pergunta (objeto) 
""" for v in pessoa.values():
    print(v) """
""" for k in pessoa.keys():
    print(k) """


""" pessoa['Nome'] = 'Fredy' # Substituir nome 
pessoa['Peso'] = 98.0 # adicionar no dicionário
for k,v in pessoa.items():
    print(f'{k}-----{v}') """

estado = dict()
portugal = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    portugal.append(estado.copy())
print()
print()

for e in portugal:
    for v in e.values():
        print(v, end='  ')

    print()
    print()
