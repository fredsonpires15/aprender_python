"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em
um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer."""

import random

computador = random.randint(0, 10)
palpites = 0  # por enquanto ele não deu palpites nenhum
certo = False  # certo recebe Falso ou seja, pode ser que ele ainda não acertou
while not certo:  # enquato ele não acertar,
    jogada = int(input("Digite um número num intervalo de 0 a 10:"))  # ele vai ler um número
    palpites += 1  # e vai somar um palpite ou uma jogada
    if jogada == computador:  # se o jogador for igual ao computador,
        certo = True  # acertou
    else:  # e se não for igual vai executar o que esta em baixo
        if computador > jogada:
            print("Mais...Tente mais uma vez")
        elif computador < jogada:
            print("Menos...Tente mais uma vez")
print("Você acertou depois de {} tentativas!!".format(palpites))