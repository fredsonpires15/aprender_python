#Exercício - Lista de tarefas com desfazer e refazer
#Música para codificar =)
# Todo mundo quer governar o mundo - Lágrimas por medos
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
import json


class Tarrefa:

    def __init__(self,tarefa, tarefas, refazer_tarefas):
        self._tarefas = tarefas
        self._refazer_tarefas = refazer_tarefas
        self._tarefa = tarefa
        
        
    
    def listar(self):
        if not self._tarefas:
            print('Nenhuma tarefa para listar')
            return
        
        print('Tarefas: ')
        for tarefa in self._tarefas:
            print(f'\t {tarefa}')
    
    def desfazer(self):
        print()
        if not self._tarefas:
            print('Nenhuma tarefa para desfazer')
            return
        
        tarefa = self._tarefas.pop() 
        self._refazer_tarefas.append(tarefa)
        print(' Tarefa desfeita com Sucesso...')

    def refazer(self):
        print()
        if not self._tarefas:
            print('Nenhuma tarefa para refazer')
            return
        
        tarefa = self._refazer_tarefas.pop()
        self._tarefas.append(tarefa)
        print(' Tarefa Refeita com Sucesso...')

    def adicionar(self):
        print()
        tarefa = self._tarefa.strip()
        if not tarefa:
            print('Você não digitou uma tarefa.')
            return
        self._tarefas.append(tarefa)
        print('Tarefa Adicionada com Sucesso...')

# Depois faz esta parte numa file a parte
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8' ) as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print(' Arquivo não existe!! ')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo): 
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8' ) as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

    return dados 
      
CAMINHO_ARQUIVO = 'ficheiro.json'
tarefas = ler([], CAMINHO_ARQUIVO)
print(tarefas)
refazer_tarefas = []


while True:
    tarefa = input('Digite uma Tarrefa ou Comando: ')
    print('Comandos: listar, desfazer e refazer')

    """ if tarefa == 'listar':
        t = Tarrefa(tarefa, tarefas, refazer_tarefas) # criar uma instância da classe Tarefa
        print('============="================')
        t.listar()  # Chamar o método 'listar'  da instância
        print('============="================')

    elif tarefa == 'desfazer':
        t = Tarrefa(tarefa, tarefas, refazer_tarefas)
        t.desfazer()
        print('============="================')
        t.listar()  # Chamar o método 'listar'  da instância
        print('============="================')

        continue

    elif tarefa == 'refazer': 
        t = Tarrefa(tarefa, tarefas, refazer_tarefas)
        t.refazer()
        print('============="================')
        t.listar()  # Chamar o método 'listar'  da instância
        print('============="================')

        continue

    elif tarefa == 'clear':
        os.system('cls')
        continue

    else:
        t = Tarrefa(tarefa, tarefas, refazer_tarefas)
        t.adicionar()
        print('============="================')
        t.listar()  # Chamar o método 'listar'  da instância
        print('============="================')

        continue """
    

    t = Tarrefa(tarefa, tarefas, refazer_tarefas) # criar uma instância da classe Tarefa
    # Usando o dicianario para evitar condicionais
    comandos = {
        'listar': lambda: t.listar(), 
        'desfazer':lambda: t.desfazer(), 
        'refazer':lambda: t.refazer(), 
        'clear':lambda: os.system('cls'), 
        'adicionar':lambda: t.adicionar(), 
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)




#p = Tarrefa
#print(p)
    






        
