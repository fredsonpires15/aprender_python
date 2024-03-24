"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Resolução
"""
num = (input('Degite um número inteiro: '))
num_par = num % 2 == 0
if num_par:
    print('O número {num} é PAR!!')
else:
    print('O número {num} é  IMPAR!!')
 
# outra forma de resolver
try: # ou if num.isdigit():
    num_int = int(num)
    par_impar = num_int % 2 == 0
    par_impar_texto = 'IMPAR'

    if par_impar:
        par_impar_texto = 'PAR'


    print(f'O número {num_int} é {par_impar_texto}')

except: # ou else:
    print('Você não degitou um número inteiro')
"""


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# resolução

entrada = (input('Diga-me que horas são:'))


try:
    hora = int(entrada)
    de_manha = hora >= 0 and hora <= 11

    a_tarde = hora >= 12 and hora <= 17

    a_noite = hora >= 18 and hora <=23
    if de_manha:
        print('Olá, Bom dia !!')
    elif a_tarde:
        print('Olá, Boa Tarde!!')
    elif a_noite:
        print('Olá, Boa Noite!!')
    else:
        print('Horário inválido!!') 
except:
    print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Resolução

# nome = str(input('Degite seu primeiro nome:'))
# num_letras = len(nome)
# if num_letras <= 4:
#     print('Seu nome é curto')
# elif 5 <= num_letras <= 6:
#     print('Seu nome é normal')
# else:
#     print('Seu nome é muito grande')
