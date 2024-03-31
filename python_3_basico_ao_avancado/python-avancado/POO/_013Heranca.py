
# Herança simples - Relações entre classes
# Associação - EUA, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Turma principal (Pessoa)
# -> superclasse, classe base, classe pai
#Aulas filhas (Cliente)
# -> subclasse, classe filha, classe derivada

class Pessoa:
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    
    def falar_nome_classe(self):
        print(f'{self.nome} {self.sobrenome} - {self.__class__.__name__}')


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Nem saí a da classe Cliente!!')
        print(f'{self.nome} {self.sobrenome} - {self.__class__.__name__}')


class Aluno(Pessoa):
    ...

c1 = Cliente('Fredson', 'Vila Nova')
c1.falar_nome_classe()

a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()

#help(Cliente)




























