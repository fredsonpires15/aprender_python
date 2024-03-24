from math import sqrt
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = sqrt(pow(co, 2) + pow(ca, 2))
print("O comprimento da hepotenusa é {:.2f} ".format(h))

