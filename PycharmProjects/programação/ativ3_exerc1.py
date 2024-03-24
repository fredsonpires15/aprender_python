from math import ceil

exame = float(input("Nota do exame:"))
pro = float(input("Nota do projeto:"))
if exame >= 10:
    nfinal = (exame * 70 / 100) + (pro * 30 / 100)
    print("A nota fina é \033[36m{}".format(ceil(nfinal)))
else:
    print("\033[33m{}".format(ceil(exame)))
