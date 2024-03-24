""" Vamos adicionar uma variável de classe chamada
empCount na classe Employee. Para cada objeto declarado, 
o método __init__() é chamado automaticamente. Este método 
inicializa as variáveis ​​de instância e também incrementa empCount em 1. """

class Employee:
    empCount = 0

    def __init__(self, name, age):
        self.__name= name
        self.__age = age
        Employee.empCount += 1

        #print('Name:',self.__name, 'Age:',self.__age)
        #print("Employee Number:", Employee.empCount)
    '''   
    def showcount(self):
        print(f'foram {self.empCount} ciclo(s)')
    
    counter = classmethod(showcount)
    """ classmethod(instance_method) - transforma um metodo de instância 
    em um método de classe que pode ser chamado com referencia à classe e não ao objeto  """
    '''

    # Usar o decorador '@classmethod()' é a maneira prescrita de definir um método de classe


    """ classmethod
    def showcount(cls):
        print(f'foram {cls.empCount} ciclo(s)') """


    # O método de classe atua como um construtor alternativo.
    # Defina um método de classe newemployee() com argumentos necessários para construir um novo objeto. 
    # Ele retorna o objeto construído, algo que o método __init__() faz.
    @classmethod
    def showcount(cls):
        print(f'foram {cls.empCount} ciclo(s)')
        return
    
    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

    

e1 = Employee("Fredy",21)
e2 = Employee("Edy", 19)
e3 = Employee("Edson", 24)
e4 = Employee.newemployee('Ana', 23)


#e1.showcount()
#Employee.counter()
Employee.showcount()

print()
