# Exemplo 1:
c = 0  # o c começa com 1
while c < 11:  # enquanto o contador for menor do que 10
    print(c)  # mostra contador (c)
    c += 1  # porque quando ele volta, vai somar mais 1
print("FIM")

# e quando eu não sei o limite?
# exemplo 2:
"""n = 1  # n começa com 1
while n != 0:  # enquanto o n for diferente de zero (0)
    n = int(input("Digite um número:"))  # ele vai ficar lendo um número qualquer
print("FIM!!")"""

# exemplo 3:
""""r = "S" or "N"
while r == "S" or r == "N":

    r = str(input("Quer continuar? [S/N]")).upper()
print("FIM!!")"""
# exemplo 4:
# número par ou impar
"""n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um número:"))
    if n != 0:  # só vai funcionar se o que está dentro for diferente de zero(0)
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Ao todo tivemos {} números par e {} números impares".format(par, impar))"""
