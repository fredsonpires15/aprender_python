import turtle as tur
import colorsys as cs
 
tur.setup(800, 800)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor('black')
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'brown', 'cyan']



for i in range(50):
    for j in COLORS:
        for k in COLORS:
            tur.color()
            tur.right(90)
            tur.circle(200-i*4,90)
            tur.color(j,k)
            tur.left(90)
            tur.circle(200-i*4,90)
            tur.right(180)
            tur.circle(50,24)
            tur.color()


tur.hideturtle()
tur.done()
