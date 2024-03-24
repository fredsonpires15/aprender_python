
""" Métodos de classe - São metodos onde ' self' será 
'cls', ou seja, ao invés de receber a instância no primeiro
parametro, recebemos a própria classe. """


class Pessoa:
    ano = 2023  # atributo da class

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_class(cls):
        print('Hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):  
        return cls('Anônima', idade)


p1 =  Pessoa('joão', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(23)


print(p2.nome , p2.idade)
print(p3.nome , p3.idade)
print(p4.nome , p1.idade)



#print(Pessoa.ano)
#Pessoa.metodo_de_class()


