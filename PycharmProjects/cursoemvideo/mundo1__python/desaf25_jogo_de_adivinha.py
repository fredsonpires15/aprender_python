from random import randint
from time import sleep
import emoji
print("_"*20)
print("""Jogo de adivinha""")
print("_"*20)
print("""Eu vou pensar num número entre 0 e 5, e tu vais tentar adivinhar qual número eu pensei!""")
num = int(input("Tentar adivinhar o número que eu pensei: "))   # jogador vai pensar num número
it = randint(0, 5)    # o computador vai pensar num número
print("processando...")
sleep(3)   # tempo para processar e dar a resposta
if it == num:
    print(emoji.emojize("Parabens! Você venceu o jogo:scream::scream::clap:", language="alias"))
else:
    print(emoji. emojize("Sinto muito! você perdeu:sunglasses:", language="alias"))
    print(emoji.emojize("Pensei no número {}! :grinning::laughing::laughing: ".format(it), language="alias"))
