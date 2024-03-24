"""x = 10
y = 3
z = 0
while x >= y:
   x = x - y
   z = z + 1
print(z)"""

"""iter = int(input("ne:"))
soma = 0
while iter != 0:
    soma = soma + iter
    iter = iter - 1
print(iter)"""
"""
x = 12
y = 6
while y != 0:
    z = x % y
    x = y
    y = z
print(x)"""

"""n = int(input("digite um número inteiro:"))
conta = 0
while n > 0:
    if n % 2 == 0:
        conta += 1
    n -= 1
print("Os números pares menores ou iguais a {} são {} ".format(n, conta))"""

"""def fun():
    n1 = 4
    print(f'N1 detro vale {n1}')


n1 = 3
fun()
print(f'N1 fora vale {n1}')
str"""


def media_melhores_tres(n1, n2, n3, n4):
    if n1 < n2 and n3 and n4:
        soma = n2 + n3 + n4
    elif n2 < n1 and n3 and n4:
        soma = n1 + n3 + n4
    elif n3 < n1 and n2 and n4:
        soma = n1 + n2 + n4
    elif n4 < n1 and n2 and n3:
        soma = n1 + n2 + n3
    else:
        soma = n1 + n2 + n3

    media = soma / 3
    return media


media = media_melhores_tres(1, 1, 1, 1)
print(media)
