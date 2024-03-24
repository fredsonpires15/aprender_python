"""
Cálculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.: 746.824.890-70 (746824890)
   10 9 8 7 6 5 4 3 2
* 7 4 6 8 2 4 8 9 0
   70 36 48 56 12 20 32 27 0
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obtenha o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

import re
import sys

""" cpf_enviado_pelo_cliente = ("952.484.770-18" .replace('.', '')
                                             .replace('-', '')
                                             .replace(' ', '')
                                                             ) """

entrada = input(' ')
cpf_enviado_pelo_cliente = re.sub(
    r'[^0-9]', # substituir qualquer coisa  de 0 a 9 que não seja um número
      '',       # para nada   
    
    entrada)


contador = 10
somar = 0

try:
    entrada_sequencial = entrada == entrada[0] * len(entrada)

    if entrada_sequencial:
        print('Você enviou dados sequenciais.')
        sys.exit()

    nove_digitos = cpf_enviado_pelo_cliente[:9]


    for digito in nove_digitos:
        mult = contador * int(digito)
        contador -= 1
        somar += mult   
        mult_som_10  = somar * 10
    rest_divisao1 = mult_som_10 % 11
    rest_divisao1 = rest_divisao1 if rest_divisao1 <= 9 else 0


    # calcular o segundo digito
    dez_digitos = nove_digitos + str(rest_divisao1)
    contador = 11 # agora começa com 11
    somar = 0
    for digito in dez_digitos:
        mult = contador * int(digito)
        contador -= 1
        somar += mult   
        mult_som_10  = somar * 10
    rest_divisao2 = mult_som_10 % 11
    rest_divisao2 = rest_divisao2 if rest_divisao2 <= 9 else 0


    cpf_criado_pelo_comp = f"{nove_digitos}{rest_divisao1}{rest_divisao2}"

    if cpf_criado_pelo_comp == cpf_enviado_pelo_cliente:
        print(f'{cpf_criado_pelo_comp} CPF é valido')
    else:
        print(f'{cpf_criado_pelo_comp} CPF é inválido')

except NameError:
    print('voce não digitou um número')
except IndexError:
    print('Você não digitou nenhum CPF')