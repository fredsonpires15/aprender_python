"""
dividir e juntar com lista e str
split - divide uma string (lista)
join - uma string
"""
frase  =  ' Olha só que , coisa interessante '
lista_frases =  frase.split (',')


nova_lista = []
for i, frase in enumerate(lista_frases):
    nova_lista.append(lista_frases[i].strip())

#print(nova_lista)

frases_unidas = '___'.join(lista_frases)
print(frases_unidas)