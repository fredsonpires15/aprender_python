
def mdc(m,n):
    """
    Calcular o máximo divisor comum de dois inteiros
    """
    if m%n==0:
        return n
    else:
        return mdc(n, m%n)


class Racional:
    def __init__(self, numerador, denominador=1):
        min_div_comum = mdc(numerador, denominador)
        self.numer : int = int(numerador / min_div_comum) 
        self.deno : int = int(denominador / min_div_comum
) 
    def __str__(self):
        if self.deno == 1:
            return f'{(self.numer)}'
        else:
            return f'{self.numer}/{self.deno}'
    

    def __add__(self, other):
        novo_numer = self.numer * other.deno + self.deno * other.numer
        novo_deno = self.deno * other.deno

        return Racional(novo_numer, novo_deno)
    
    __radd__ = __add__

    

    def __mul__(self, other):

        if isinstance(other, int):
            other = Racional(other)
        novo_numer = self.numer * other.numer 
        novo_deno = self.deno * other.deno

        return Racional(novo_numer, novo_deno)
    
    __rmul__=__mul__


    def __truediv__(self, other):
        if isinstance(other, int):
            other = Racional(other)
        novo_numer = self.numer * other.deno
        novo_deno = self.deno * other.numer
        return Racional(novo_numer, novo_deno)
    
    def __sub__(self, other):

        if isinstance(other, int):
            other = Racional(other)
        novo_numer = self.numer * other.deno - self.deno * other.numer 
        novo_deno = self.deno * other.deno

        return Racional(novo_numer, novo_deno)
    
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return
        
        else:
            return (self.numer==self.deno) and  (self.deno==self.deno)
    
    def __lt__(self, other):
        extremos = self.numer * other.deno
        meios = self.deno * other.numer
        return extremos < meios 
    





if __name__ == '__main__':
    frac_1 = Racional(5,5)
    frac_2 = Racional(3,6)

    frac_3 = frac_1 + frac_2
    frac_5 = frac_1 - frac_2
    frac_4 = frac_1 / 4  
    frac_5 = frac_1.__lt__
    

    print(frac_3)
    print(frac_4)
    print(frac_5)
    