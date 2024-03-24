from time import sleep
dis = float(input("Qual é a distância da viagem em km:"))
sleep(1)
print("Você esta prestes a fazer uma viagem de {}km.".format(dis))
sleep(1)
print("A calcular o preço da sua viagem...")
sleep(3)
preco1 = dis * 0.50
preco2 = dis * 0.45
if dis <= 200:
    print("O preço da viagem é de {:.2f}Euros".format(preco1))
else:
    print("O preço da viagem  é de {:.2f}Euros".format(preco2))
print("Bom dia! tenha uma boa viagem.")
