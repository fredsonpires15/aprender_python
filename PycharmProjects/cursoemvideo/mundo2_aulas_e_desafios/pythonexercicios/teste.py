"""def obter_pessoa():
    lista = ["Fredson", "Teixeira", 19]
    return f'Primeiro nome:{lista[0]} \n' f'Último nome:{lista[1]}\n' f'Idade: {lista[2]}'


print(obter_pessoa())"""


def obter_pessoa():
    nome = input("Seu primeiro nome:")
    apelido = input("Apelido:")
    idade = input("Sua idade:")
    pessoas = [nome, apelido, idade]
    return pessoas


def outra_pessoa():

    print("Primeiro nome:{pessoas[0]} {pessoas[1]}\n Idade: {pessoas[2]}")
    print("Primeiro nome:{pessoas[0]} {pessoas[1]}\n Idade: {pessoas[2]}")


pessoas = obter_pessoa()
outra_pessoa()