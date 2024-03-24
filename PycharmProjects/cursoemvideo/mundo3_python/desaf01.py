"""Crie um programa que tenha uma dupla totalmente 
preenchida com uma contagem por extenso,
 de zero até vinte. Seu programa deverá ler um 
 número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso"""

num_0_a_20 = (0,1, 2, 3, 4,
              5, 6, 7, 8,
              9, 10, 11,12
              ,13,14,15,16
              ,17,18,19,20)
num_por_extenso = ('zero','um','dois','três','quatro','cinco',
                   'seis', 'sete','oito','nove','dez',
                   'onze', 'doze', 'treze', 'catorze',
                   'quinze',  'dezaseis',  'dezasete',
                   'dezoito',  'dezanove', 'vinte'

 )


while True:
    num = input('digite um número entre (0 e 20): ')
    if int(num) in num_0_a_20:
        print(f'Você digitou o número {num_por_extenso[num_0_a_20[int(num)]]}')
        
    else:
        print('Tente novamente. digite um número entre (0 e 20)')

    continuar = input('Quer continuar? sim[s]/ Não[n]: ').upper() 
    if continuar == 'N':
        break
       
    

