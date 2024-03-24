print("\033[33m:\033[m"*25)
print("\033[34m    10 primeiros termos")
print("\033[33m:\033[m"*25)
"""termo = int(input("Primeiro termo: "))
razao = int(input("Razão:"))
cont = 0
for c in range(1, 11):
    pA = termo + (c - 1) * razao
    cont += 1
    print("\033[33m {} \033[m".format(pA), end=" -» ")
print("FIM!")"""
# Outra forma de fazer este código  é a seguinte:
termo = int(input("Primeiro termo:"))
razao = int(input("Razão:"))
cont = 0
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print("{}".format(c), end=" ->")
print("FIM!!")