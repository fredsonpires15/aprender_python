"""
args -  argumentos não nomeados
- *args (empacotamento e desempacotamento)
"""

# lembre_te de desempacotamento

x, y, *resto = 1, 2, 3, 4

def soma(*args):
    for numero in args:
        print(numero)



soma(1,2,3,4)