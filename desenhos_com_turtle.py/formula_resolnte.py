import math

def formula_resolvente(a,b,c):

    delta = b**2 - 4*a*c

    if delta < 0: 
        print('A sua equação não tem Raiz!!')

    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b- math.sqrt(delta))/(2*a)

        return f'X1 = {x1:.2f}, X2 = {x2:.2f}'

a= 2
b= 6
c= 1

raizes = formula_resolvente(a,b,c)

print(f'As raizes são: {raizes}')

