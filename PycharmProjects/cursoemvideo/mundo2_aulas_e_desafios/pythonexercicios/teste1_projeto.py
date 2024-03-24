import turtle
import random


# criar janela
def janela():
    tela = turtle.Screen()
    tela.setup(largura, altura)
    tela.title("Jogo corrida de tartaruga")


# criar tela com linhas
def criar_tela_com_linha():
    janela()
    espaco_entre_linhas = largura / linhas  # espaços entre as linhas
    linha = turtle.Turtle()
    for i in range(linhas):  # para cada i inteiro em um conjunto de numero _ "linhas"
        pos_inicial_linha = -largura / 2 + (i + 1) * espaco_entre_linhas - ((largura / linhas) / 2)
        # Vai enumerrar as linhas
        if i == 0:
            linha.left(90)
        linha.penup()  # permite que a caneta vá para cima
        linha.setx(pos_inicial_linha - pos_inicial_linha * (bordo / 100))
        linha.sety((-altura / 2 + (altura / 2) / 2) - (-altura / 2 + (altura / 2) / 2) * (
                    bordo / 100))  # posição da linha coordenada,y)
        linha.pendown()  # perminte que as linhas apareçam e que se
        linha.color("green")
        linha.pensize(4)
        linha.fd(((altura - (altura * (bordo / 100))) / 2))  # traçar uma linha para frente (altura da linha)
        linha.write("F" if i == linhas - 1 else i, align="center", font=("Arial", 14))


ponto = 0.0
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'brown', 'cyan']


# criar turtarugas
def criar_tartarugas(COLORS):
    tartarugas = []
    # definir a posição das tartarugas no eixo xx
    posicao_tart_xx = -(largura / linhas) * linhas / 2 + largura / (2 * linhas)
    espaco_entre_tart = (altura / 2) / num_de_tartarugas  # define o espaço entre as tartarugas
    for i, color in enumerate(COLORS):  #
        posicao_inicial_tart_eixo_y = (-altura / 2 + (i + 1) * espaco_entre_tart + (
                    ((num_de_tartarugas - 2) / 2) + 0.5) * espaco_entre_tart)
        tart = turtle.Turtle()
        tart.color(color)
        tart.shape('turtle')  # apresentar a tartaruga na tela
        tart.rt(0)  # para virar a horizonal
        tart.penup()
        tart.setpos(posicao_tart_xx - posicao_tart_xx * (bordo / 100),
                    posicao_inicial_tart_eixo_y - posicao_inicial_tart_eixo_y * (bordo / 100))
        tart.pendown()
        tartarugas.append(tart)
    return tartarugas


pont = turtle.Turtle()


def quadro_pontuacao():
    quadro = turtle.Turtle()
    pos_x = (min(altura, largura) / 4) / 2  # posição da caixa de eixo xx
    pos_y = altura / 4 + altura / 12
    quadro.color("black")
    quadro.penup()
    quadro.goto(pos_x / 2, pos_y)  # corresponde ao posicionamento segundo (x,y) do quadrado
    quadro.pendown()
    quadro.color("black")
    for i in range(4):
        quadro.fillcolor("yellow")
        quadro.left(90)
        quadro.fd(pos_x)  # corresponde ao comprimento necessario para formar o quadrado
    quadro.hideturtle()


def pontuacao(ponto):
    pont.penup()
    pont.goto(-min(altura, largura) * 0.025 * 2,
              (altura / 4 + altura / 8))  # corresponde ao posicionamento da palavra "ponto" segundo (x,y) do quadrado
    pont.pendown()
    pont.write(f"Pontos:  \n  {ponto}", font=(
    'Time New Roman', int((min(altura, largura)) / (1 / (min(altura, largura) * 0.025) * (min(altura, largura)))),
    'normal'))
    pont.hideturtle()


def quadro_record():  # fazer um retângulo para pôr o "ponto máximo"
    larg_do_retang = (min(altura, largura) / 4) / 2
    pont_max = turtle.Turtle()
    pont_maxx = -(largura / 2) + (largura / 8) / 2
    pont_maxy = altura / 4 + altura / 12
    pont_max.penup()  # movimentar (levantar) a caneta
    pont_max.goto(pont_maxx, pont_maxy)  # posição (x,y) do retângulo
    pont_max.pendown()  # descer a caneta para escrever novamente
    # pronto para desenhar novamente
    pont_max.fd(larg_do_retang + larg_do_retang)
    pont_max.left(90)
    pont_max.fd(larg_do_retang)
    pont_max.left(90)
    pont_max.fd(larg_do_retang + larg_do_retang)
    pont_max.left(90)
    pont_max.fd(larg_do_retang)
    pont_max.hideturtle()
    #  Definir a posição da palavra "ponto máximo"


letra = turtle.Turtle()


def nome_record(nome):  # definimos outra variável porque outra não nos facilita
    pont_maxx = -(largura / 2) + (largura / 8) / 2
    letra.penup()
    letra.goto(pont_maxx, altura / 4 + altura / 8)
    letra.pendown()
    letra.write(f"  Ponto Máximo: \n  {nome}| {ponto_max}",
                font=('Time New Roman', int((min(altura, largura)) / (1 / (min(altura, largura)
                                                                           * 0.025) * (min(altura, largura)))),
                      'normal'))
    letra.hideturtle()


# difinir a escolha da tartarugas
def correr():
    distancia = (largura / linhas) * (linhas - 1) / 2 - ((largura / linhas) * (linhas - 1) / 2) * (bordo / 100)
    while True:
        for velocista in tartarugas:
            velocidade = random.randint(1, 5)  # o valor da velocidade escolhido aleatoriamente
            velocista.forward(velocidade)  # permite as tartarugas avançarem para frente
            velocista.clear()

            x = velocista.xcor()
            if x >= distancia:
                return COLORS[tartarugas.index(velocista)]


def atualizar_pontos():
    pontuacao(ponto)
    quadro_record()
    exit()


with open("ficheiro_de_jogo.txt") as ficheiro:
    linh = ficheiro.readline()
    dados_do_jogo = linh.split(",")

    largura, altura, linhas = int(dados_do_jogo[0]), int(dados_do_jogo[1]), int(dados_do_jogo[2])
    bordo = int(dados_do_jogo[3])
    num_de_tartarugas = int(dados_do_jogo[4])
    nome_records = str(dados_do_jogo[5])
    ponto_max = float(dados_do_jogo[6])


# definir uma função para fazer as tartarugas regressarem as suas posicões inicial
def recuar():
    # calcular as pos-xx das tartarugas
    posicao_tart_xx = -(largura / linhas) * linhas / 2 + largura / (2 * linhas)
    espaco_entre_tart = (altura / 2) / num_de_tartarugas  # espaçamento entre elas
    for i, tartaruga in enumerate(tartarugas):  # para cada tartaruga dentro da lista enumerada
        posicao_inicial_tart_eixo_y = (-altura / 2 + (i + 1) * espaco_entre_tart + (
                    ((num_de_tartarugas - 2) / 2) + 0.5) * espaco_entre_tart)  # posicção-y das tartarugas

        tartaruga.setpos(posicao_tart_xx - posicao_tart_xx * (bordo / 100),
                         posicao_inicial_tart_eixo_y - posicao_inicial_tart_eixo_y * (bordo / 100))
        tartaruga.clear()


op = 0
if 2 <= num_de_tartarugas <= 8:
    # seleciolar as tartarugas que vão jogar
    selecionar_tart = COLORS[:num_de_tartarugas]
    criar_tela_com_linha()  # função que faz
    # definir uma variável que recebe uma lista com tartarugas
    tartarugas = criar_tartarugas(selecionar_tart)  # as lista com tartarugas
    # programa só vai parar de rodar quando a opção for 2

    quadro_pontuacao()
    pontuacao(ponto)
    quadro_record()
    nome_record(nome_records)
    # rodar o jogo
    while True:
        while True:  # lupe infinito
            cor_tart = str(input("Diga a cor da tartaruga que vai ganhar {}:".format(COLORS[:num_de_tartarugas])))
            if cor_tart not in COLORS[
                               :num_de_tartarugas]:  # se a cor escolhida não estiver dentro desta lista de cores
                print("A cor não está nas opções.Tente novamente!!")  # mostrar na tela
            else:
                break  # interromper o ciclo
            continue  # continuar o jogo
        # definir um variável que recebe a vencedora
        vencedora = correr()
        if vencedora == cor_tart:  # se a vencedora for igual a cor escolhida
            print("Você venceu o jogo . . .")
            ponto += 1  # contar mais um ponto
        else:
            print("--------\033[31mPerdeu o jogo!!\033[m---------")
            if ponto > 0:
                ponto -= 0.5  # tirar 0.5 pontos
        pont.clear()  # Apagar o anterior
        pontuacao(ponto)  # A atualizar o ponto
        # Fazer um  Menu para de opção
        print("»»««»»«« MENU »»««»»««")
        print("Escolha uma opção: \n \033[32:1m[1] -\033[m iniciar o jogo\n \033[31:1m[2] - \033[mSair do jogo  ")
        op = int(input("Sua Opção: "))
        if op == 2:  # se a opção for "2" o jogo vai terminar
            if ponto > ponto_max:  # quando o ponto for maior que o ponto_max
                ponto_max = ponto  # o ponto_max vai receber o valor do ponto
                nome_records = str(input("Parabens! Até agora você tem a pontuação mais alta.\nDiga o seu nome: "))
                letra.clear()  # Ele vai apagar o nome da pessoa que tinha a pontuação máxima anterior
                nome_record(nome_records)  # acrestar nome da pessoa que tem o novo  ponto máximo
                print("\033[31mFIM do jogo!!\033[m")
            # Atualizar o ficheiro  e colocar os dados dentro de ficheiro
            with open("ficheiro_de_jogo.txt", "w") as ficheiro:
                ficheiro.write(f"{largura},{altura},{linhas},{bordo},{num_de_tartarugas},{nome_records},{ponto_max}")
            break  # interromper o jogo
        else:
            recuar()  # quando as tartarugas chegarem a meta esta função fará com elas regressam as suas posição iniciais
elif num_de_tartarugas < 2:
    telinha = turtle.Screen()
    telinha.bgcolor("orange")
    telinha.setup(largura, 100)
    telinha.title("Jogo corrida de tartaruga")
    turtle.color("green")
    turtle.goto(-200, 0)
    turtle.write("NÚMERO DE TARTARUGAS INSUFICIENTE. ESCOLHA UM Nº ENTRE (2 - 8)!")
    turtle.hideturtle()
else:
    telinha = turtle.Screen()
    telinha.bgcolor("orange")
    telinha.setup(largura, 100)
    telinha.title("Jogo corrida de tartaruga")
    turtle.color("green")
    turtle.goto(-200, 0)
    turtle.write("NÚMERO DE TARTARUGAS EM EXCESSO. ESCOLHA UM Nº ENTRE (2 - 8)!")
    turtle.hideturtle()