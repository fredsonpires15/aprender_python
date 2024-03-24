
import sys
import matplotlib.pyplot as plt


with open("ficheiro_de_jogo.txt") as ficheiro:
    event_data = ficheiro.readline().strip().split()

dados = []
lista = event_data

for dado in lista:  
    print(dado)


# Plotando os dados do evento
#plt.plot(event_data)
plt.xlabel('Tempo')
plt.ylabel('Movimento')
plt.title('Movimento da espaçonave ao longo do tempo')
plt.show()
