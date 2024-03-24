
# ecrever uma função que devolva o máximo divisor comum
def mdc(m,n):
    while m%n != 0:
        mvelho = m
        nvelho = n

        m = nvelho
        n = mvelho % nvelho
    return n


class Fraction:


    def __init__(self, cima, baixo):

        self.numerador = cima
        self.denominador = baixo
    

    """ def show(self):
        return f'{self.numerador}/{self.denominador}'
    """
    # '__str__', é o método para converter um objeto em uma string

    def __str__(self):
        return f'{str(self.numerador)} / {str(self.denominador)} '
    

    def __add__(self, other):
        novonum = self.numerador*other.denominador + self.denominador*other.numerador
        novoden = self.denominador * other.denominador
        divisor_comum = mdc(novonum, novoden)

        return Fraction(novonum // divisor_comum, novoden // divisor_comum)


    def __eq__(self, other: object):
        primeiro = self.numerador * other.denominador
        segundo = other.numerador* self.denominador
        return primeiro == segundo
    



    
""" class LogicGate:
    
    def __init__(self, n) -> None:
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self,n)

        self.pinA = None 
        self.pinB = None 

    def getPinA(self):
        return int(input('Digite a entrada do Pino A para a Porta '+ self.getLabel() +'-->'))
    

    def getPinB(self):
        return int(input('Digite a entrada do Pino B para a Porta '+ self.getLabel() +'-->'))

class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a==1 and b==1:
            return 1
        else:
            return 0

class Connector:


    def __init__(self, fgate, tgate):
        self.formgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.formgate
    
    def getTo(self):
        return self.togate
    

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else: 
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('Erro: NÃO HÁ PINO LIVRE')
            
 """

myfraction = Fraction(4,5)
f1 = Fraction(1,4)
f2 = Fraction(1,2)

f3 = f1 + f2
#print(myfraction.show())
print(myfraction)
print('resposta:',f1==f2)

print(f'{f1}+ {f2}= {f3}') 


""" porta = AndGate('G1')

print(porta.getOutput()) """






