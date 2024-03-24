lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
"""for comida in lanche:
    print(f"Eu vou comer {comida}")
print("comi pra caramba!!")"""
# podemos fazer também usando (len())
"""for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')"""

# A outra forma de fazer é usando o (enumerate):
"""for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicão {pos}")"""

# Uma outra coisa que pode ser feita é: (por ex:)
"""print(sorted(lanche))  # (sorted) é para organizar as coisas
print(lanche)"""
# Outra coisa também que pode ser feita é por exemplo:

"""a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
# print(c)
# print(len(a)) # ->  podemos usar o (len()) também
# print(c.count(5))  # count -> (vai indicar quantas vezes o nº5 aparece dentro de (c))
# print(c.index(4))  # index -> (vai indicar em que posição esta o nº4"""
# também podemos deletar a tupla inteira:
"""pessoa = ('fredy', 22, 'M', 68.9)
del(pessoa)  # Não pedemos apagar um elemento dentro da tupla, mais podemos apagá-la inteira"""

