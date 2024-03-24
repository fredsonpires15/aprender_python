""" Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato. """

aproveitamento = dict()
listagols = list()
jogador = str(input("Nome do jogador: "))

partidas = int(input(f"Quantas portidas {jogador} jogou? "))
totalgols = 0
for i in range(partidas):
    gols = int(input(f"Quantos gols tevi na {i+1}º partida? "))
    totalgols += gols
    listagols.append(gols)
print(f'lista de gols: {listagols} \nTotal de gols no Campeonato: {totalgols} ')
aproveitamento['nome'] = jogador
aproveitamento['golos'] = listagols
aproveitamento['TotaldeGolos'] = totalgols
print()
print()

print('-='*30)
print(aproveitamento)
print('-='*30)

print()

print('-='*30)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)

print()

print('-='*30)
print(f'O jogador {jogador} jogou {partidas} partidas. ')
for pos, gol in enumerate(listagols):
    print(f'   => Na {pos+1}º partida, fez {gol} gols')
print('-='*30)

print()
print()

