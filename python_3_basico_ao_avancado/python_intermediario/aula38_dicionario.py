# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Luiz',

    'sobrenome': 'Miranda', 
}

""" print(p1['nome'])

print(p1.get('sobrenome'))

nmoe=p1.pop('nome')

print(nmoe)

print(p1) """

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 24
# })

# p1.update(nome=' novo valor', idade= 30)
# tupla = (('nome','novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['iade', 30]]

# p1.update(lista)
# print(p1)

# facil = [valor **1 for valor in range(1,10001)]
# print(facil)

""" players = ['charles', 'martina','michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
print('jogar\'bola\'')
b = 'b\tc\nd\fe'
print(b) """

# mylife = open(r'C:new text.txt', 'w')
# print(mylife)
path = r'C:new text.dat', 'w'
print(path)
