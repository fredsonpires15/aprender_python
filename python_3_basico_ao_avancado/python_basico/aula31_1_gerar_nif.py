"""O NIF tem 9 dígitos, sendo o último o digito de controlo.
 Para ser calculado o digito de controlo:

Multiplique o 8.º dígito por 2, o 7.º dígito por 3,
 o 6.º dígito por 4, o 5.º dígito por 5, o 4.º dígito por 6,
o 3.º dígito por 7, o 2.º dígito por 8 e o 1.º dígito por 9;
Some os resultados;
Calcule o resto da divisão do número por 11;
Se o resto for 0 (zero) ou 1 (um) o dígito de controlo será 0 (zero);
Se for outro qualquer algarismo X,
 o dígito de controlo será o resultado da subtracção 11 - X."""
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

print(nif_criado_pelo_comp)
