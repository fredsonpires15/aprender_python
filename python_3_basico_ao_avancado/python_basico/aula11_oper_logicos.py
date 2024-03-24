# operadores lógicos
# and (e), or (ou), not (não)
# and - todas as condições precisam ser verdadeiras.
# se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# também existe o tipo "None" que é usado para
# representar um não valor
#if 1 and 1:
    #print(True and 1 and False)

# operadores in e not in 
# Strings são iteráveis
# 0 1 2 3 4 5 
# o t á v i o
# -6-5-4-3-2-1
# nome = 'otávio'
# # print(nome[0])
# print('á' in nome) # está em nome ?
# print('to' in nome) # 'to' está em nome
# print('-'*10)
# print('á' not in nome) # 'á' não está em nome
# print('teu' in nome) # "teu" está em nome 
"""variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)"""
#


#  interpolação básica de Strings
# s - strings
# d e i - int
# f - float
#  x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Luiz'
preco = 1000.95873
variavel = '%s, o preço é %.2f€' % (nome, preco)
print(variavel)
print('o Hexadecimal de %d é %08X' % (201, 201)) 



