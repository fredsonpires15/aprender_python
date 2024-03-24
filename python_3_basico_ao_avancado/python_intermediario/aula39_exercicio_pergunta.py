# sistema de pergunta e resposta
import random
from time import sleep 



def calcular(num1,num2,operacao):
  if   operacao == '+':
    return f'{num1+num2}'
  elif operacao == '-':
    return f'{num1-num2}'
  else:
    return f'{num1*num2}'
  
# Organizar a lista
def organizar(num1,num2,operacao):
    if   operacao == '+':
      op = [f'{num1+num2}',f'{num1+num2-1}', f'{num1+num2 +4}',f'{num1+num2-2}']
      return op
    elif operacao == '-':
      op = [f'{num1-num2}',f'{num1-num2-1}', f'{num1-num2 +4}',f'{num1-num2-2}']
      return op
    else:
      op = [f'{num1*num2}',f'{num1*num2-1}', f'{num1*num2 +4}',f'{num1*num2-2}']
      return op
    
def aper(num1, num2, operacao,perguntas):
  if operacao == '+':
    return f'{num1} + {num2} = {perguntas["Resposta"]} '
  elif operacao == '-':
    return f'{num1} - {num2} = {perguntas["Resposta"]} '
  else:
    return f'{num1} x {num2} = {perguntas["Resposta"]} '
  
pontos = 0.0


ponto_max = 0.0

while True: 
    operacao = random.choice(['+','-', '*'])
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    op1 = organizar(num1,num2,operacao)   
    random.shuffle(op1)   # desorganizar lista
    opcoes = op1
    resultado = calcular(num1, num2, operacao)
    
    perguntas = {
        'Pergunta':f'Quanto é {num1} {operacao} {num2}:',
        'opcao': f'{opcoes}',
        'Resposta': f'{resultado}'
        }
    mostrar_resultado = aper(num1, num2, operacao, perguntas)
    print()
    print('perguntas:', perguntas['Pergunta'])
    print()
    
    for ind,valor in enumerate(opcoes):
      print(f'{ind+1}) {valor:>2}')
    print("")

    escolha = input('Escolha uma opção: ')
    # converter para int
    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)

    print(" ")

    if escolha.isdigit():
      escolha_int = int(escolha)

      if escolha_int < 0 or  escolha_int>4:
         print('Não existe esta opção!! TENTE OUTRA VEZ.')
         sleep(3)
         continue
      
      if opcoes.index(opcoes[escolha_int-1]) == opcoes.index(perguntas['Resposta']):
        print('PARABÉNS!! És Muito bom a Matemática.')
        pontos += 10
      else:
        print('ERRADO!! Tens Que dar uma olhada na Tabuada')
        if pontos > 0:
          pontos -= 5

      print(mostrar_resultado)
    else:
      print('Degite apenas número indicado na opção!!')

    # if escolha_int is not None:
    #   if escolha_int >= 0 and escolha_int< qtd_opcoes:
    #     if opcoes[escolha_int] == perguntas['Resposta']:
    #       acertou = True
    #print(opcoes.index(opcoes[escolha_int])==opcoes.index(perguntas['Resposta']))
      
    sair = str(input('Quer continuar? [Sn/Nn]: '))
    if sair.upper() == 'N':
      if pontos > ponto_max:  # quando o ponto for maior que o ponto_max
        ponto_max = pontos  # o ponto_max vai receber o valor do ponto
        nome_records = str(input(f"Parabens! Até agora você tem a pontuação mais alta: {ponto_max} pontos .\nDiga o seu nome: "))
      print("\033[31mFIM do jogo!!\033[m")
            # Atualizar o ficheiro  e colocar os dados dentro de ficheiro
      with open("sistema_pergunta_resp.txt", "w") as ficheiro:
        ficheiro.write(f"RECORD:\nNome: {nome_records} \nPonto: {ponto_max}")
      break


print(f'Você obteve:  {pontos} pontos')
  
  

    
