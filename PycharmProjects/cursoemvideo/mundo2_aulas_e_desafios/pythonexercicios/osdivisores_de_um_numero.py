n = int(input("Digite um valor:"))
cont = 0
for i in range(1, n - 1):
    if n % i == 0:
        print(f"{i}", end=" ")
        cont += 1
print(cont)