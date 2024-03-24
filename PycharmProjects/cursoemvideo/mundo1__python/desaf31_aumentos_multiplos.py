s = float(input("Qual é o salário do funcionário?"))
# calculando o aumento salarial
if s > 1250:
    au = s + (s * 10 / 100)
else:
    au = s + (s * 15 / 100)
print("se você ganha {:.2f}euros passará a ganhar {:.2f}Euros".format(s, au))

