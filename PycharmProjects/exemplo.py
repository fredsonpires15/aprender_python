from random import randint
from skimage import io, color, filters


def atirar_dado():
    dado1 = io.imread("dice1.png")
    dado2 = io.imread("dice2.png")
    dado3 = io.imread("dice3.png")
    dado4 = io.imread("dice4.png")
    dado5 = io.imread("dice5.png")
    dado6 = io.imread("dice6.png")
    todos = [dado1, dado2, dado3, dado4, dado5, dado6]
    escolha = choice(todos)
    io.imshow(escolha)
    io.show()


atirar_dado()
