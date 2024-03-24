from time import sleep
valor = float(input("Valor da casa:"))
salario = float(input("QUal o seu salário:"))
anos = int(input("Em Quantos anos deseja pagar:"))
prest = valor / (12 * anos)
print("A analizar os dados....")
sleep(2)
print("\033[1:37m Para pagar a casa de {:.2f}Euros  em {} anos,".format(valor, anos), end="")
print(" a prestação será de {:.2f}euros mensais ".format(prest))
if prest <= salario * 30 / 100:
    print("\033[35m-=-\033[m" * 20)
    print("          \033[32:1m Empretimo consedido!!\033[m      ")
    print("\033[35m-=-\033[m" * 20)
else:
    print("\033[35m«»\033[m" * 20)
    print("\033[31:1m     Emprestimo negado!!     \033[m")
    print("\033[35m«»\033[m"*20)
