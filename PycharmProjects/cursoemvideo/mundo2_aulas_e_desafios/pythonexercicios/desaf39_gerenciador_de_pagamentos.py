print("\033[1:36m»»««»»««»»« \033[1:32m SUPERMERCADO VINO,L.d.a \033[1:36m»««»»««»»«\033[m")
preco = float(input("Preço das compras:"))
print("Como pretende fazer o pagamento:")
print("""\033[1:30:42m[1] \033[m-» \033[1:37mà vista dinheiro/cheque
\033[1:30:41m[2] \033[m-» \033[1:37mà vista cartão
\033[1:30:43m[3] \033[m-» \033[1:37m em até 2x no cartão 
\033[1:30:44m[4] \033[m-» \033[1:37m 3x ou mais no cartão """)
opc = int(input("\033[1:39:40m Sua opção:\033[m"))
if opc == 1:
    dis = preco - (preco * 10 / 100)
    print("\033[1:33mCom esta opção você passa a ganhar um desconto de 10%.\033[m ")
    print("Sua compra de \033[1:33m{:.2f}Euros\033[m vai passar a custar "
          "\033[1:33m{:.2f}Euros\033[m no total".format(preco, dis))
elif opc == 2:
    dis = preco - (preco * 5 / 100)
    print("\033[1:33m Escolhendo esta opção você passa a ganhar 5% de desconto\033[m")
    print("Sua compra de \033[1:33m{:.2f}Euros\033[m vai passar a custar"
          " \033[1:33m{:.2f}Euros\033[m no total.".format(preco, dis))
elif opc == 3:
    parc = int(input("Pagamento em quantas parcelas?"))
    if parc <= 2:
        p = preco / parc
        print("Sua compra de {:.2f}Euros em {} parcelas vai costar {}Euros".format(preco, parc, p))
    else:
        print("\033[1:31m INVALÍDO...\033[mTente novamente!!")
elif opc == 4:
    print("Optando por esta opção estarás sujeito a uma taxa de juros de 20%.")
    parc = int(input("Deseja pagar em quantas parcelas? :"))
    if parc >= 3:
        pjuros = preco + (preco * 20 / 100)
        p = pjuros / parc
        print("Fizeste uma compra de {:.2f}euros,"
              " e com a taxa de juros será de {:.2f}Euros".format(preco, pjuros))
        print("O pagamento  será de {:.2f}Euros com Juros em {} parcelas".format(p, parc))
else:
    pjuros = 0
    print("Fizeste uma compra de {:.2f}euros, "
          "e com a taxa de juros será de {:.2f}Euros".format(preco, pjuros))
    print("\033[1:31mINVALÍDO!!\033[m.Por favor, Tente novamente.")