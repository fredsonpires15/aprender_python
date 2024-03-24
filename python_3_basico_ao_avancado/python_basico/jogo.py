import turtle
import random

# Configurações do jogo
WIDTH = 700
HEIGHT = 500
FONT = ("Arial", 24, "normal")
COLORS = ["red", "blue", "green", "yellow", "purple"]

# Cria a janela do jogo
window = turtle.Screen()
window.title("Corrida de Tartaruga")
window.setup(WIDTH, HEIGHT)

# Cria as tartarugas
num_turtles = 5
turtles = []
for i in range(num_turtles):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(COLORS[i % len(COLORS)])
    t.penup()
    t.goto(-WIDTH/2 + 20, (HEIGHT/2 - 50) - i*30)
    turtles.append(t)

# Cria o texto de resultado
result = turtle.Turtle()
result.hideturtle()
result.penup()
result.goto(0, HEIGHT/2 - 50)
result.write("Corrida de Tartaruga!", align="center", font=FONT)

# Inicia a corrida
winner = None
while not winner:
    for t in turtles:
        distance = random.randint(1, 10)
        t.forward(distance)
        if t.xcor() >= WIDTH/2 - 20:
            winner = t.color()[0]
            break

# Mostra o resultado
result.clear()
result.write("Vencedor: {}!".format(winner.upper()), align="center", font=FONT)

# Mantém a janela aberta até o usuário fechar
turtle.done()