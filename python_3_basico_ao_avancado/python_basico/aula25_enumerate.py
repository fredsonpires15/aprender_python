""" enumerate - enumera iteráveis(índices) """
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Fredy')

#lista_enumerada = list(enumerate(lista, start= 2)) # enumera cada item da lista
#print(lista_enumerada)

for indice, nome in enumerate(lista): # para cada tupla, ele separa o indice e o nome
    print(indice, nome)
    