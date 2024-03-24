"""file = open("abc.txt", "w+")  # w+ -> abrir um arquivo para leitura e escrita
file.write("linha 1\n")  # ecrever coisas dentro desse arquivo
file.write("linha 2\n")
file.write("linha 3\n")
file.write("linha 4\n")

print(file.read())


file.close() """ # fechar o arquivo



"""a_list = [1, 2, 3, 4]
print(a_list)

while len(a_list) > 0:
    element = a_list.pop()
    print(element)

print(a_list)"""


# linhas para corrida
import turtle

t = turtle.Turtle()
turtle.Screen()
t.speed()
for i in range(0, 600, 200):
    t.pencolor('grey')
    t.penup()
    t.setpos(-200 + i , -200)
    t.pendown()
    if i == 0:
        t.left(90)

    t.fd(400)
    t.bk(400)
