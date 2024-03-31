
""" Python também possui uma super()função que 
fará com que a classe filha herde todos os métodos e 
propriedades de sua classe pai: 

Ao usar a super()função, você não precisa usar o nome do elemento pai, 
ela herdará automaticamente os métodos e propriedades de seu pai
"""

class PessoaEsloca:
    def __init__(self,numero, nome):
        self._numero = numero
        self._nome = nome

    def obtem_numero(self):
        return self._numero
    
    def obtem_nome(self):
        return self._nome

class Aluno(PessoaEsloca):
    ...

class Funcionario(PessoaEsloca):
    def __init__(self, numero, nome, salario):
        super().__init__(numero, nome)
        #PessoaEsloca.__init__(self, numero, nome)
        self._salario = salario

    def obtem_salario(self):
        return self._salario
    
#uma classe pode estar ligada a mais do que uma uma SuperClasse. É pois, possível a situação seguinte 

class C1:
    def canta(self):
        return False

class C2:
    def voa(self):
        return True
    
class C3(C1, C2):
    pass 

if __name__ == '__main__':
    pesc = Funcionario(49895, 'Fredson Vila Nova -', 2500)
    print(pesc.obtem_nome(), pesc.obtem_salario())
    print('|-------------------------------------------|')
    print()
    a1 = C3()
    print(a1.canta(), a1.voa())
    print()

















































