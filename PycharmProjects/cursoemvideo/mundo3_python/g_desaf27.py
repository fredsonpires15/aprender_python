""" 
Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior
 """
lista = (12,	72,11,	66,14,	84,10,	60,17,	102,11,	66,11,	66,14,	84,13,	78,0,	0,11,	66,16,	96,
)
#def maior(num):
def maior(*num):
    cont = maior = 0
    
    for valor in num:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Ao todo foram contados {cont} valores \nE o maior é {maior}')
         



maior(1,12,3,4,5,6,7,6,7,8,7,7,8,9,66,5,)
maior(23,44,424,35,567,23,56,57,467,67,4,67,468,4346,55,57,58,57,89,58,478,5,58,653,4)
maior(7)
#maior(lista)
