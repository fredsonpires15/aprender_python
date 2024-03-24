
""" Uma pilha é uma coleção ordenada de objetos
em que os últimos elementos a serem inseridos são 
também os primeiros a serem retirados """

class EmptyStack(Exception):
    """ Tentativa de aceder a um contentor vazio..."""
    pass

class Stack:
    def  __init__(self):
        self.stack = []

    def __str__(self):
        saida = ''
        for elem in self.stack[::-1]:
            saida = str(elem) + ',' + saida
        saida = saida[:-1]
        return '[' + saida + ']'
         

    def push(self, object):  # acrescentar elementos
        self.stack.append(object)

    def pop(self): # função que eliminar elementos
        if self.is_empty(): # se consultamos uma pilhe vazia, resulta num ERRO
            raise EmptyStack('ERRO: acesso e modificação de uma pilha vazia!')
        return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            raise EmptyStack('ERRO: Consulta de uma pilha vazia!...')
        else:
            return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    

    
if __name__ == '__main__':
    p1 = Stack()
    p1.push(3)
    p1.push('BARR')
    p1.push({'Nome': 'Ana'})
    p1.push([1,2,3,6])
    p1.pop
    print(p1)

    
    
    