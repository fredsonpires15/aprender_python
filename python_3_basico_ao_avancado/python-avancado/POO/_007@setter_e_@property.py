

class Caneta:
    def __init__(self, cor):
        self._cor = cor

    """ def get_cor(self):
        print('Cor')
        return self.cor_tinta """
    @property
    def cor(self):
        #print('apenas esta a mostrar na tela')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Este já é um SETTER: ', valor)
        self._cor = valor


      
    
   

""" def mostrar(caneta):
    return caneta.cor """

caneta = Caneta('Green')
caneta.cor = 'VERMELHA'
print(caneta.cor)
#mostrar(caneta)