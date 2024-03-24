"""Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando
  o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

nome = str(input("Qual é o seu nome?"))
vencido = 0
while True:
    jogador = int(input("Joga um valor:"))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("PAR ou IMPAR? [P/I]")).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}...', end="")
    print("DEU PAR " if total % 2 == 0 else "DEU IMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu!!")
            vencido += 1
        else:
            print("--------GAME OVER!!----------")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você Venceu!!")
            vencido += 1
        else:
            print("--------GAME OVER!!----------")
            break
    print("»«" * 15)
print(f"{nome} você  foi vencedor {vencido} vez(es)")
# Os dois são os têm o mesmo código
print("<>«»"*10)


from random import randint

nome = str(input("Qual o seu nome?"))
ven = 0
while True:
    jogador = int(input("joga um valor:"))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("PAR OU IMPAR? [P/I] ")).upper().strip()[0]
    print(f"O {nome} jogou {jogador} o computador {computador}. Um total de {total}...", end="")
    print("DEU PAR!!" if total % 2 == 0 else "DEU IMPAR!!")
    if tipo == "P":
        if total % 2 == 0:
            print("Você Venceu!!")
            ven += 1
        else:
            print("você perdeu!!!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você Venceu!!")
            ven += 1
        else:
            print("Você Perdeu!!")
            break
    print("__" * 10)
print(f"{nome} foi vencedor {ven} vezes")
