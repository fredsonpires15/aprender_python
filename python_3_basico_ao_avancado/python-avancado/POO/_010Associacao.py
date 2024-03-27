
# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None


    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    
   
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    
    @staticmethod
    def soma(x, y):
        return f'{x} x {y} = {x*y}'



escritor = Escritor('Carlos')
caneta = FerramentaDeEscrever('Caneta ferramenta de escrever')
maquina_de_escrever = FerramentaDeEscrever('Maquina de escrever é muito boa')

escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(escritor.ferramenta.escrever()) 
print(escritor.ferramenta.soma(3,7)) 




















