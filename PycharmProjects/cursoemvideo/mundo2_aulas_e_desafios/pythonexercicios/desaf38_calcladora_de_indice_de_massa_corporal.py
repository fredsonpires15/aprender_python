print("\033[1:35m«»"*38)
print("""\033[1:39:40m Lembre-se que a Organização Mundial de Saúde recomenda                    \033[m
\033[1:39:40m que você mantenha seu IMC entre 18,5 e 24,9. Nunca exagere pois           \033[m
\033[1:39:40m estar abaixo do peso ideal para sua altura também deve ser evitado,       \033[m
\033[1:39:40ma magreza excessiva também é uma doença.                                   \033[m""")
print("\033[1:35m«»\033[m"*38)
p = float(input("Seu peso:"))
a = float(input("Sua altura:"))
imc = p / a ** 2
if imc < 18.5:
    print("\033[1:33m IMC: \033[1:31m{:.1f}\033[m -»\033[1:34m Abaixo do peso".format(imc))
elif 18.5 <= imc < 25:
    print("\033[1:34m IMC: \033[1:31m{:.1f} \033[m-»\033[1:32m PESO IDEAL".format(imc))
elif 25 <= imc < 30:
    print("\033[1:34m IMC: \033[1:31m{:.1f}\033[m -» \033[1:33m SOBREPESO".format(imc))
    print("""»» Quer dizer que tem mais peso do que é considerado em
relação ao peso normal ou saudável para a idade ou tamanho.""")
elif 30 <= imc < 40:
    print("\033[1:34m IMC: \033[1:31m{:.1f}\033[m -»\033[1:35m OBESIDADE".format(imc))
else:
    print("\033[1:34m IMC: \033[1:32m {:.1f}\033[m -» \033[1:31m OBESIDADE MÓRBIDA".format(imc))