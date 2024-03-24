"""  """
""" Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. """
Time = list()
aproveitamento = dict()
listagols = list()


while True:
    jogador = str(input("Nome do jogador: "))
    totalgols = 0
    listagols.clear()
    partidas = int(input(f"Quantas portidas {jogador} jogou? "))
    aproveitamento.clear()
    for i in range(partidas):
        listagols.append(int(input(f" => Quantos gols teve na {i+1}º partida? ")))
   
    aproveitamento['nome'] = jogador
    aproveitamento['golos'] = listagols[:]
    aproveitamento['TotaldeGolos'] = sum(listagols)
    Time.append(aproveitamento.copy())
    
    while True:
        sair = str(input('Quer continuar? [S/N]: ')).upper()
        if sair in 'SN':
            break
    if sair == 'N':
        break
print()
print()
# print(Time)
print('-='*30)
print('  Nº ', end='')
for k in aproveitamento.keys():
    print(f' \033[1:32m {k:<15}\033[m', end='')
print()
print('-='*30)
for ind, dic in enumerate(Time):
    print(f'{ind:>3}', end=' ')
    for v in dic.values():
        print(f'   {str(v):<15}', end='')
    print()
print('-='*30)
print()
print()
print('-='*30)
while True:
    buscar = int(input(" Mostrar dados de qual jogador? (999 para parar): "))
    if buscar==999:
        break
    if buscar >= len(Time):
        print('Não existe jogador com este Nº')
    else:
        print(f'--- levantamento de dados do jogador {Time[buscar]["nome"]}')
        for pos , gols in enumerate(Time[buscar]['golos']):
            print(f'    No {pos+1}º jogo {Time[buscar]["nome"]} fez {gols} golos')
    print('-='*30)
print()
print('«« Volte Sempre »»')
print()
print()

