from turtle import *
import math
from random import *
lista = []
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'brown', 'cyan']
def haerta(a):
    return 15*math.sin(a)**3
def heartb(a):
    return 12*math.cos(a)-8*\
            math.cos(2*a)-4*\
            math.cos(3*a)
            #math.cos(4*a)-\
            #math.cos(4*a)
speed(1000)
bgcolor('black')
for i in range(1, 6000, 5):
    goto(haerta(math.sqrt(i*20)), heartb(math.sqrt(i*20)))
    lista.append(randint(i,600))
    
    for j in COLORS:
        color('#f73487')
        #color(j)
    goto(0,0)
print(lista)

done()


