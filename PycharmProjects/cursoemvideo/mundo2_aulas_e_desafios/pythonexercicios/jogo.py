from turtle import Screen, Turtle
from random import randint

STAMP_SIZE = 20
SQUARE_SIZE = 15
FINISH_LINE = 200
LANE_WIDTH = 50

BIG_FONT = ('Arial', 40, 'bold')
MEDIUM_FONT = ('Arial', 30, 'bold')

COLORS = ['black', 'cyan', 'magenta', 'yellow', 'white']


def play():
    pen.clear()

    lane = LANE_WIDTH

    for n, color in enumerate(COLORS, start=1):
        turtl = turtles[color]
        turtl.hideturtle()
        turtl.goto(-250, n // 2 * lane)
        turtl.showturtle()

        lane = -lane

    # Asking user to play

    user_bet = None

    while user_bet not in COLORS:
        print("Please choose one colour out of", *["\n" + color.title() for color in COLORS])
        user_bet = input("Place your bet on your any one colour turtle: ").lower()

    # Moving the turtles

    for _ in range(145):

        for turtl in turtles.values():
            distance = randint(1, 5)
            turtl.forward(distance)

    # Deciding the winner

    winner = max(turtles, key=lambda x: turtles[x].xcor())

    pen.clear()
    if user_bet == winner:
        pen.write("You won the bet!", align='center', font=MEDIUM_FONT)
    else:
        pen.write("You lost the bet.", align='center', font=MEDIUM_FONT)


# Screen

screen = Screen()
screen.title("Turtle Race")
screen.bgcolor('forestgreen')

turtle = Turtle()
turtle.hideturtle()
turtle.speed('fastest')
turtle.penup()

# Dirt

turtle.setposition(-400, -180)
turtle.color('chocolate')

turtle.begin_fill()
for _ in range(2):
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
turtle.end_fill()

# Finish line

turtle.color('black')
turtle.shape('square')
turtle.shapesize(SQUARE_SIZE / STAMP_SIZE)

for i in range(10):
    turtle.setposition(FINISH_LINE, 150 - i * SQUARE_SIZE * 2)
    turtle.stamp()
    turtle.setposition(FINISH_LINE + SQUARE_SIZE, (150 - SQUARE_SIZE) - i * SQUARE_SIZE * 2)
    turtle.stamp()

turtle.setposition(0, 200)
turtle.write("Turtle Race", align='center', font=BIG_FONT)

pen = Turtle()
pen.hideturtle()
pen.color('blue')
pen.penup()
pen.setposition(0, 50)

turtle_prototype = Turtle()
turtle_prototype.hideturtle()
turtle_prototype.shape('turtle')
turtle_prototype.speed('fastest')
turtle_prototype.penup()

turtles = {}

for color in COLORS:
    turtle = turtle_prototype.clone()
    turtle.color(color)
    turtles[color] = turtle

choice = 'yes'

while choice.lower() in ('y', 'yes'):
    play()

    choice = input("Do you want to play again?\nPress y for yes and n for no: ")
