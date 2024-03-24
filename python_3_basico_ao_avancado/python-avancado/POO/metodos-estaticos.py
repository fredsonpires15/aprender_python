
class Employee:
    empCount = 0

    def __init__(self, name="Fredy", age='21'):
        self.__name= name
        self.__age = age
        Employee.empCount += 1

    """ Um '@staticmethod' em Python é um decorador usado para definir 
    um método na classe que não requer acesso à instância da classe (self) 
    nem à classe (cls). Em outras palavras, ele é usado para criar métodos 
    que não dependem do estado do objeto ou da classe em si.

class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b   
    
    
    
    """
    @staticmethod
    def showcount():
        print(f'foram {Employee.empCount} ciclo(s)')
        return
    

    

e1 = Employee("Fredy",21)
e2 = Employee("Edy", 19)
e3 = Employee("Edson", 24)

# Não é necessário instanciar a classe Calculadora para usar os métodos estáticos
# print(Calculadora.soma(5, 3))        # Saída: 8
# print(Calculadora.subtracao(10, 7))  # Saída: 3

e1.showcount()
Employee.showcount()
print(hasattr(e1, 'salary'))
#setattr(e1, 'salary', 7000)
#delattr(e1, 'age')
#print(e1.__age)

print()
