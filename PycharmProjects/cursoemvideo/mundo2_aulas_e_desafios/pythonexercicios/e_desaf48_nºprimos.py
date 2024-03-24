num = int(input("Digite um número:"))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[32m ", end=" ")
        cont += 1

    else:
        print("\033[33m ", end=" ")
    print("{}".format(c), end=" ")
if cont == 2:
    print("\n \033[mComo o número {} apresenta apenas {} devisores;".format(num, cont))
    print(" Portanto é número PRIMO. ")
else:
    print("\n \033[mComo o número {} apresenta mais de dois devisores;".format(num))
    print("Logo, não é número PRIMO.")
