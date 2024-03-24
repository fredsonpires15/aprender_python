from math import sqrt
xa, ya = eval(input("\033[36m introduza as coordenadas do ponto A, separadas por vírgulas:"))
xb, yb = eval(input("introduza as coordenadas do ponto B, separadas por vírgulas:"))
d = sqrt(pow((xb - xa), 2) + pow((yb - ya), 2))
print("A distância entre A e B =\033[33m {:.2f}".format(d))
