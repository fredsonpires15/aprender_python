
# Módulo collectinos - counter(contador)
from collections import Counter

"""
 lista = [1,2,1,2,3,45,6,7,6,7,8,9,87,6,5,4,23,44,56,43,5,64,56,35,3]
Exemplo 1:

# utilizando o counter
res = Counter(lista)
print(type(res))

print(res)
# Counter({6: 3, 1: 2, 2: 2, 3: 2, 7: 2, 5: 2, 56: 2, 45: 1, 8: 1, 9: 1, 87: 1, 4: 1, 23: 1, 44: 1, 43: 1, 64: 1, 35: 1})

Exemplo 2:

print(Counter('Eu não gosto de comer muito'))
#Counter({' ': 5, 'o': 5, 'u': 2, 't': 2, 'e': 2, 'm': 2, 'E': 1, 'n': 1, 'ã': 1, 'g': 1, 's': 1, 'd': 1, 'c': 1, 'r': 1, 'i': 1})

# Exemplo 3:

texto = ''' tem que ter estrutura, elementos que estabelecem relação entre si.
Dentro dos aspectos formais temos a coesão e a coerência, que dão sentido
e forma ao texto. A coesão textual é a relação, a ligação, a conexão entre as
palavras, expressões ou frases do texto. A coerência está relacionada com 
a compreensão, a interpretação do que se diz ou escreve. Um texto precisa ter 
sentido, isto é, precisa ter coerência. Embora a coesão não seja condição 
suficiente para que enunciados se constituam em textos, são os elementos coesivos
que lhes dão maior legibilidade e evidenciam as relações entre seus diversos componentes,
a coerência depende da coesão.'''

palavras =  texto.split()

# print(palavras)

res = Counter(palavras)
print(res)
print()
print(res.most_common(5))

"""


# Módullo collections - defaultdict
from collections import defaultdict
""" 
dicionario = defaultdict(lambda:0)

dicionario['Nome:']= 'Fredson'
dicionario['Apelido:']= ' Vila Nova'

print(dicionario)
print(dicionario['outro']) # seria KeyError no dicionairo comum, mas aqui não!



# Módulo Collections - ordered dict

from collections import OrderedDict


dicionario = OrderedDict({'a': 1, 'b':2 ,'c': 2,'d':3})
for chave, valor in dicionario.items():
    print(f'chave={chave}; valor={valor}')

 """


"""Módulo collections - Named Tuple"""

# recap tuple 
 

# Importando 
from collections import namedtuple 

# precisamos de definir o nome e parâmetro

# forma 1 - declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - declaração 
cachorro1 = namedtuple('cachorro','idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro2 = namedtuple('cachorro', ['idade','raca', 'nome'])

# Usando
ray = cachorro1(idade=22, raca='Bela', nome='Fredson')


print(ray)

# acessar os dados 
# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])
print()
# Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)
