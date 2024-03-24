from time import sleep

vel = float(input("Diga a velocidade do carro:"))
mul = 7 * (vel - 80)
print("Processando...")
sleep(3)
if vel > 80:
    print("Limite de velocidade ultrassada de acordo com o 1ºartg.lei/2022 ")
    print("Com os dados obtidos a multa rescisória será de {}Euros".format(mul))
else:
    print('Meus agradecimentos!')
    print("Respeitando as regras do transito, estarás a respeitar a sua vida!!!")
