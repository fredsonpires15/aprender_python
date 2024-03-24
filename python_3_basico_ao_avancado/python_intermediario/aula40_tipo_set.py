# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3} 
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('Olá mundo',)) # adiciona varios valores
# s1.add(91)
# s1.discard('Luiz') # eliminar luiz
# print(s1)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

# importante lembrar que, além de não gtermos vallores duplicados , não temos ordem

""" lista = [99,34,23,2,12,34,44,5]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99,34,23,2,12,34,44,5)
print(f'Tupla:{tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99,34,23,2,12,34,44,5], 'dict')
print(f'Dicionairo: {dicionario} com {len(dicionario)} elementos')

sets = {99,34,23,2,12,34,44,5}
print(f'Set: {sets} com {len(sets)} elementos') """

# remover elementos
""" 
s1.remove(3)
print(3) """
 
 # imagine que temos dois conjuntos: um contendo estudantes de python e 
 # contendo estudantes de Java
estud_pyhton = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estud_java = {'Fredson','Gustavo','Julia','Ana','Patricia'}

# Tem alunos que estão nos dois cursos!

# Gerar um conjunto com nomes de estudantes  únicos

# forma_1 - utilizando 'union'

""" unir = estud_pyhton.union(estud_java)
print(unir)

# forma 2 - Utilizando caracte pipe '|'

unir2 = estud_pyhton | estud_java
print(unir2) """

# Gerar  um conjunto de estundantes que estão em ambos os cursos
""" # Forma 1 - utilizando 'itersection'
ambos1 = estud_pyhton.intersection(estud_java)
print(ambos1)
# Forma 2 - utilizando &
ambos2 = estud_pyhton & estud_java
print(ambos2) """

# Gerar um conjunto de estudante que não estão no outro curso

""" so_java = estud_java.difference(estud_pyhton)
print(so_java)

so_python = estud_pyhton.difference(estud_java)
print(so_python) """

















