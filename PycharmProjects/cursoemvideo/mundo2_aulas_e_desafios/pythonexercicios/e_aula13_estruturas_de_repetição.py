# i = int(input("Início:"))
# f = int(input("FIM:"))
# p = int(input("Passo:"))
# for c in range(i, f + 1, p):
#   print(c)
# print("FIM.")

s = 0
for c in range(0, 3):
    n = int(input("Digite um valor:"))
    s = s + n  # ou s += n -» seria a mesma coisa
print("O somatório de todos os valores foi {}".format(s))
print("FIM!")
