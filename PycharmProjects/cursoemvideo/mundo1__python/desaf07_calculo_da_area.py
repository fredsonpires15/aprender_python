# Calculo da àrea e a quantidade de tinta necessaria para pintar uma parede
l = float(input("Qual é a largura da parede em metros: "))
a = float(input("Qual é a altura da parede em metros: "))
area = l * a
tinta = area / 2
print("A parede tem uma àrea de {} metros quadrados".format(area))
print("Com a àrea de {} metros quadrados, seria necesserio {} litros de tinta".format(area, tinta))


