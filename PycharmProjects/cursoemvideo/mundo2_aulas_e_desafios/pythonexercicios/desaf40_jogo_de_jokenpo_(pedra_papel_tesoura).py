from random import randint
from time import sleep

print('\033[1:30m*************\033[1:33m GAME \033[1:30m************')
lista = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
print("{:^39}".format("\033[4:31m   JOKENPÔ\033[m"))
print("\033[1:32:4mSuas Opções:\033[m")
print("""\033[1:39:47m[0]\033[m -» \033[1:37mPedra
\033[1:39:40m[1]\033[m -» \033[1:39mPapel
\033[1:39:43m[2]\033[m -» \033[1:36mTesoura""")
print(
    "\033[35m:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
jogador = int(input("\033[1:39:7mQual é a sua jogada? :\033[m"))
print(" \033[1:31m  JO")
sleep(1)
print(" \033[1:32m  KEN")
sleep(1)
print("  \033[1:33m PÔ!!")
print("-«»" * 10)
if computador == 0:  # computador joga pedra
    if jogador == 0:
        print("\033[1:32mComputador jogou: \033[1:37m{}".format(lista[computador]))
        print("\033[1:33mJogador jogou: \033[1:37m{}".format(lista[jogador]))
        print("\033[1:34mO jogo foi um EMPATE")
    elif jogador == 1:
        print("\033[1:35mComputador jogou: \033[1:36m{}".format(lista[computador]))
        print("\033[1:33mJogador jogou: \033[1:37m{}".format(lista[jogador]))
        print("\033[1:32mO jogador ganhou!!. \033[1:39mPorque o papel embrulha a pedra")
    elif jogador == 2:
        print("\033[1:32mComputador jogou: \033[1:39m{}".format(lista[computador]))
        print("\033[1:33mJogador jogou: \033[1:36m{}".format(lista[jogador]))
        print("\033[1:31mO computador ganhou!! \033[1:37mPois a pedra pode amassar ou quebrar a tesoura.")
    else:
        print("\033[1:31mOpção inválida!!\033[m Tente novamente.")
elif computador == 1:  # computador joga papel
    if jogador == 0:
        print("\033[1:32mComputador jogou: \033[1:39m{}".format(lista[computador]))
        print("\033[1:33mJogador jogou: \033[1:36m{}".format(lista[jogador]))
        print("\033[1:31mComputador ganhou!! \033[1:37mPois o papel embrulha a pedra.  ")
    elif jogador == 1:
        print("\033[1:35mComputador jogou:\033[1:39m {}".format(lista[computador]))
        print("\033[1:33mJogador jogou:\033[1:39m {}".format(lista[jogador]))
        print("\033[1:34mJogo EMPATADO!!")
    elif jogador == 2:
        print("\033[1:35mComputador jogou: \033[1:39m{}".format(lista[computador]))
        print("\033[1:33mJogador jogou:\033[1:36m {}".format(lista[jogador]))
        print("\033[1:32mO jogador ganhou!! \033[1:37mA tesoura corta o papel.")
    else:
        print("\033[1:31mOpção inválida!!\033[m Tente novamente.")
elif computador == 2:  # computador joga Tesoura
    if jogador == 0:
        print("\033[1:35mComputador jogou:\033[1:36m {}".format(lista[computador]))
        print("\033[1:33mJogador jogou:\033[1:37m {}".format(lista[jogador]))
        print("\033[1:32mO jogador ganhou!! \033[1:39mA pedra amassa ou quebra a tesoura")
    elif jogador == 1:
        print("\033[1:32mComputador jogou: \033[1:36m{}".format(lista[computador]))
        print("\033[1:33mJogador jogou: \033[1:39m{}".format(lista[jogador]))
        print("\033[1:31mO computador ganhou!! \033[1:37mA tesoura corta o papel.")
    elif jogador == 2:
        print("\033[1:32mComputador jogou: \033[1:36m{}".format(lista[computador]))
        print("\033[1:33mJogador jogou: \033[1:36m{}".format(lista[jogador]))
        print("\033[1:34mJogo EMPATADO!!")
    else:
        print("\033[1:31mOpção inválida!!\033[m Tente novamente")
print("\033[33:1m-«»" * 10)
