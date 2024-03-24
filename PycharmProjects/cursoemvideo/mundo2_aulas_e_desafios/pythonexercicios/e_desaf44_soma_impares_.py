soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1  # um contador. Nesse caso ele vai contar todos os valores divisivel por três
        soma += c  # é um acomulador. aqui ele vai somar todos esses valores.
print("A soma entre os {} nº ímpares é {}".format(cont, soma))