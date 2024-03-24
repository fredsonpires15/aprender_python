""" Faça um programa que tenha uma função chamada contador(),
 que receba três parâmetros: início, fim e passo. 
 Seu programa tem que realizar três contagens através da função criada:      
a) de 1 até 10, de 1 em 1                                                          
b) de 10 até 0, de 2 em 2                                                                                                                                           
c) uma contagem personalizada """
from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
        print('O passo não pode ser zero')
        return
    if inicio < fim:
        if passo < 0:
            passo *= -1
        if passo == 1:
            passo = 1

        else:
            if passo > 0:
                passo *= 1
            if passo == -1:
                passo = -2
    
    print(f'Contgem de {inicio}  até {fim}: de {passo} em {passo}')              
    if inicio < fim:
        for i in range(inicio,fim+1, passo):
            sleep(0.5)
            print(i,end=' ')
        print('-FiM')
  
    else:
        for i in range(inicio,fim-1, passo):
            sleep(0.5)
            print(i,end=' ')
        print('-FiM')
def personalizada():
    print('»«'*len('Contagem personalizada'))
    print('Contagem personalizada: Agora é a sua vez!!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    contador(inicio, fim, passo)
    print()
    print()
contador(1, 10, 1)
contador(0, 20, 4)  
personalizada()
