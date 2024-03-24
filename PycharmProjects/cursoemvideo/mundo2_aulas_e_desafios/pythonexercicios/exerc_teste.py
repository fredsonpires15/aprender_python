from time import sleep
from typing import Union, Any

import skimage
from _socket import timeout

"""b1 = True
b2 = False
if not (b1 and b2):
    r = False
else:
    r = True

print(r)"""
"""a, b, c = eval(input(":"))
if a > b:
    if b > c:
        print(c)
    else:
        print(b)
elif a > c:
    print(c)
else:
    print(a)"""

"""def mul_ate():
    mul = 1
    cont = 1
    for c in range(1, 11):
        mul *= c
        cont += 1
    print(mul)


mul_ate()"""

"""class Controleremoto:
    def __init__(self, cor, profundidade, altura, largura):
        self.cor = cor
        self.profundidade = profundidade
        self.altura = altura
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("Diminuir o canal")


controle1 = Controleremoto("Verde", "10cm", "2cm", "3cm")
print(controle1.largura)
controle1.passar_canal("-")"""

# CRIAR UMA CLASSE PARA CLIENTES DA NETFLIX

"""class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        lista_plano = ["basic", "premium"]
        if plano in lista_plano:
            self.plano = plano
        else:
            raise Exception("Plano inválido!!")


cliente = Cliente("Fredy", "fredy@gmail.com", "basic")
print(cliente.email)"""

# ARVORE
"""def arvore(a, b):
    a1 = a.center(7, b)
    s = a*3
    a2 = s.center(7,b)
    s2 = a * 5
    a3 = s2.center(7,b)
    s4 = a * 7
    a4 = s4.center(7,b)
    s5 = a * 1
    a5 = s5.center(7,b)
    s6 = a * 1
    a6 = s6.center(7, b)
    return f"{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}"


x = arvore("ª", "-")
print(x)"""

# usar "replace" para trocar as letras
#
#
# exercicio _ Substituir as letras
"""def encode_leet(texto):
    text1 = texto.upper().replace("A", "4")
    text2 = text1.replace("B", "8")
    text3 = text2.replace("C", "<")
    text4 = text3.replace("D", "|)")
    text5 = text4.replace("E", "3")
    text6 = text5.replace("I", "1")
    text7 = text6.replace("O", "0")
    text8 = text7.replace("U", "|_|")

    return text8


texto = "Explícito é melhor que implícito"
em_leet = encode_leet(texto)
print(em_leet)"""

"""import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()

colors = ["green", "red", "pink", "red"]

for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(200-i, 100)
        turtle.lt(90)
        turtle.circle(200-i, 100)
        turtle.rt(60)
        turtle.end_fill()


turtle.mainloop()"""

"""import turtle
import colorsys

colors = ["green", "red", "pink", "red"]


def arvore(x, y, largura, pensize, cor, angle):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(angle)
    turtle.speed(0)
    turtle.pensize(pensize)
    turtle.down()
    turtle.color(cor)
    turtle.fd(largura)


def ramos_arvore(x, y, largura, pensize, hve, angle, fat_angle, n):
    if n == 0:
        return
    (r, g, b) = colorsys.hsv_to_rgb(hve, 1, 1)
    arvore(x, y, largura, pensize, (r, g, b), angle)
    tx = turtle.xcor()
    ty = turtle.ycor()

    ramos_arvore(tx, ty, largura * 0.7, pensize * 0.7, hve - 1 / 13, angle + fat_angle, fat_angle, n - 1)
    ramos_arvore(tx, ty, largura * 0.7, pensize * 0.7, hve - 1 / 13, angle - fat_angle, fat_angle, n - 1)

    turtle.tracer(10)


turtle.setup(600, 600)
turtle.title("sam codehub")
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('black')

ramos_arvore(0, -200, 100, 10, 12 / 13, 90, 25, 12)
turtle.update()
turtle.done()"""

import numpy as np
##A = np.zeros_like((3, 6))
# print(A)
# tuplo = (3, 5, 2, 7)
# v = np.array(tuplo)
# print(v)
# A = np.array([[2, 6, 3],
#        [7, 9, 1]])
# print(A[1][1])

# x = np.ones( (3, 3) ).sum()
# print(x)
# A = np.eye(3)
# B = np.array([[2, 6, 3],
#     [7, 9, 1]])
# print(A)
#matriz = np.array([[4, 5, 6],[2,3,4]])
#vet = np.array([[4, 5, 6],[2,3,4]])
#a = [0,0,0]
#c = np.vstack((matriz, vet, a))
#print(c)
print(np.random.random((3,7)), np.random.random((3,7)))