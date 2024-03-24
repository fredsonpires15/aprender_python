import turtle
import math 

lista = []

def linha(x1, y1, x2,y2):
    x = turtle
    x.up()
    x.goto(x1,y1)
    x.pd()
    x.goto(x2,y2)
    x.up()
    turtle.hideturtle()

def grafico(tartaruga, funcao,inicio, fim, n ):
    """ Desenha o grafico da função f entre inicio e fim usando n 
    segmentos."""

    # Tamanho dos segmentos 
    tam_seg = (fim -inicio )/n
    # posiciona-se
    x = inicio
    turtle.up()
    turtle.goto(x, funcao(x))
    turtle.dot(6) # pontos ao longo do grafico
    turtle.down()
     # Desenha
    
    for conta in range(n):
        x = x + tam_seg
        turtle.goto(x, funcao(x))
        lista.append(conta)
        turtle.dot(6) # pontos ao longo do grafico
        print(conta,n,x)
        
        
if __name__ == '__main__':
    turtle.setworldcoordinates(-math.pi, -2, math.pi,2)
    linha(-math.pi,0,math.pi,0)
    linha(0,-2,0,2)

    
    toto = turtle.Turtle()
    toto.pen(pensize=5, pencolor='green')
    grafico(toto, math.sin, math.pi, -math.pi, 30)
    toto.hideturtle()
    turtle.exitonclick()