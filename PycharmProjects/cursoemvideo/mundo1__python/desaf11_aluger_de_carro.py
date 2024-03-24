km = float(input(" Km percoridos:"))
dias = int(input(" Quantos dias de alugados :"))
preco = (60 * dias) + (0.15 * km)
print("O total a pagar é de {:.2f}Euros !".format(preco))
