n = int(input("Digite um número para ver sua tabuada:"))
for c in range(1, 11):
    r = n * c
    print("\033[33m{}\033[m x \033[33m{:2}\033[m = \033[34m{}".format(n, c, r))

