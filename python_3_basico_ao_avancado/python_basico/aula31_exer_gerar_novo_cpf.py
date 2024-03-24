import random


contador = 10
somar = 0

for _ in range(20):
    nove_digitos = ''
    for  i in range(9):
        nove_digitos += str(random.randint(0,9))


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

    print(cpf_criado_pelo_comp)
    