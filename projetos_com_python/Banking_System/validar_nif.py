

def check_digit(nif):
    """ Calcula o digito de controle de um NIF Ex. 99999999[0]
    >> check_digit('99999999') 
    '0'
    >> check_digit('74089837') 
    '9'
    >> check_digit('28702400') 
    '8'
    """
    if not nif.isdigit(): 
        raise ValueError
    
    contador = 9
    somar = 0
    for pos, digito in enumerate(nif):
        mult = (contador-pos) * int(digito)
        somar += mult
        #print( digito, 9-pos, pos)
    
    resto = somar % 11
    #print(resto)
    if resto == 0: return '0'
    if resto == 1: return '0'

    return str(11-resto) 
    
def validar_nif(nif):
    """ Validação do número de identificação fiscal
    >> valida_nif('999999990') 
    True
    >> valida_nif('999999999') 
    False
    >> valida_nif('501442600') 
    True
    """
    EXPECTED_DIGITS = 9
    if not nif.isdigit() or len(nif) != EXPECTED_DIGITS:
        return False
    #print(f'{nif[-1]} == {check_digit(nif[0:8])} = {nif[-1] == check_digit(nif[0:8])} ')
    return  nif[-1] == check_digit(nif[0:8])


if __name__ == '__main__': 
    val = validar_nif('308806662')
    if val:
        print(f'O número é : {val}')


""" import sys
import os


class Validar_NIF:
    def __init__(self, nif):
        self.rest_divisao1 = None
        self.nif_criado_pelo_comp = None
        self.contador = 9
        self.somar = 0
        self.oito_digitos = '' 
        self.nif_do_cliente = int(nif)


    def gerrar_nif(self):
        import random

        #oito_digitos = self.nif_do_cliente[:8]
        oito_digitos = self.nif_do_cliente
        #oito_digitos = ''
        for i in range(8):
            oito_digitos += str(random.randint(0, 9))

        contador = 9
        somar = 0
        for digito in oito_digitos:
            mult = contador * int(digito)
            contador -= 1
            somar += mult

        rest_divisao1 = somar % 11
        if rest_divisao1 == 0 or rest_divisao1 == 1:
            rest_divisao1 = 0

        else:
            rest_divisao1 = 11 - rest_divisao1
        nif_criado_pelo_comp = f"{oito_digitos}{rest_divisao1}"

        self.nif_criado_pelo_comp = f"{self.oito_digitos}{self.rest_divisao1}"
        
        #return self.nif_criado_pelo_comp
        return self.nif_criado_pelo_comp 
    
    
nif = Validar_NIF.gerrar_nif(308806662)

print(nif) """

""" def gerrar_cpf(self):
        import random
        import sys

        contador = 10
        somar = 0
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        for digito in nove_digitos:
            mult = contador * int(digito)
            contador -= 1
            somar += mult
            mult_som_10 = somar * 10
        rest_divisao1 = mult_som_10 % 11
        rest_divisao1 = rest_divisao1 if rest_divisao1 <= 9 else 0

        # calcular o segundo digito
        dez_digitos = nove_digitos + str(rest_divisao1)
        contador = 11  # agora começa com 11
        somar = 0
        for digito in dez_digitos:
            mult = contador * int(digito)
            contador -= 1
            somar += mult
            mult_som_10 = somar * 10
        rest_divisao2 = mult_som_10 % 11
        rest_divisao2 = rest_divisao2 if rest_divisao2 <= 9 else 0

        cpf_criado_pelo_comp = f"{nove_digitos}{rest_divisao1}{rest_divisao2}"

        print(cpf_criado_pelo_comp)

        self.cpf_criado_pelo_comp = f"{nove_digitos}{rest_divisao1}{rest_divisao2}"
        return self.cpf_criado_pelo_comp

    def validaar(self):
        if self.nif_criado_pelo_comp == self.cfc:
            print('CFC é Valido')
            return self.validar.setText('CPF é valido')
        else:
            return self.validar.setText(f'CPF é inválido')
 """



