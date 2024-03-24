import sympy as sp


def area_triangulo(b, h):
    """ 
        b -> base 
        h -> altura
    """
    return (b * h) / 2


def area_quadrado(lado):
    return lado ** 2


def area_retangulo(b, h):
    """ 
        b -> base 
        h -> altura
    """
    return b * h


def area_losango(D, d):
    """ 
        D -> diametro maior 
        d -> diametro menor
    """
    return (D * d) / 2


def area_trapezio(B, b, h):
    """
        B -> base maior
        b -> base menor 
        h -> altura
    """
    return ((B + b) * h) / 2


''' def calcular_derivada(f, x,h):
    """
    Função para calcular a derivada de uma função em um ponto usando a de diferença finita

    Args:
        f: Função para calcular a derivada.
        x: ponto onde a derivada será calculada
        h: Valor do incremento
    Returns:
        Apresentação da derivada da função em um ponto
    """
    return (f(x+h)- f(x)/h)

# Exemplo de função f(x)=x^2
def f(x):
    return x**2

# ponto onde a derivada será calculada 
x = 2 

# valor incremento (tamanho do passo)
h = 1

# Calcula a derivada usando a função calcular_derivada
derivada = calcular_derivada(f, x, h)

# Imprime o resultado
print("A derivada de f(x) = x^2 no ponto x =", x, "é:", derivada) '''


def derivadas():
    x = sp.Symbol('x')

    # Definindo a função
    f = x ** 3 + 2 * x ** 2 - x + 1

    # Calculando todas as derivadas
    derivadas = []
    for i in range(1, 4):
        derivada = sp.diff(f, x, i)
        derivadas.append(derivada)
        return derivadas

    """ # Imprimindo as derivadas
    for i, derivada in enumerate(derivadas):
        print(f"A {i+1}ª derivada de f(x) é: {derivada}") """


print(sp.pi)

print(sp.sin(6))
print(derivadas())
print('isso é bom de mais!!')