
import sys
import os


class Validar_NIF():
    def __init__(self):
        self.rest_divisao1 = None
        self.nif_criado_pelo_comp = None
        self.setupUi(self)
        self.contador = 9
        self.somar = 0
        self.oito_digitos = ''


    def gerrar_nif(self):
        import random

        nif_do_cliente = ''

        # oito_digitos = nif_do_cliente[:8]
        oito_digitos = ''
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
        self.nif.setText(nif_criado_pelo_comp)
        print(nif_criado_pelo_comp)

    def gerrar_cpf(self):
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
        self.cfc.setText(self.cpf_criado_pelo_comp)

    def validaar(self):
        if self.cpf_criado_pelo_comp == self.cfc:
            print('CFC é Valido')
            self.validar.setText('CPF é valido')
        else:
            self.validar.setText(f'CPF é inválido')



