from time import sleep

num = int(input("\033[42:1:30mDigite um número inteiro:\033[m"))
print("""Poderá escolher qual será a base de conversão:
\033[42:1:30m[1]\033[m -» converter para binário
\033[41:1:30m[2]\033[m -» converter para octal
\033[43:1:30m[3]\033[m -» converter para hexadecimal """)
opc = int(input("Sua opcão:"))
print("A processar dados...")
sleep(2)
if opc == 1:
    print("\033[1:32m convertendo o número\033[m"
          " \033[36m {}\033[m \033[1:32m para binário seria igual à "
          "\033[36m{}\033[m".format(num, bin(num)[2:]))
elif opc == 2:
    print("\033[1:32mConvertendo o número\033[m"
          " \033[36m {}\033[m \033[1:32m para octal seria igual à "
          " \033[36m {}\033[m".format(num, oct(num)[2:]))
elif opc == 3:
    print("\033[1:32m Convertendo o número\033[m"
          " \033[36m{}\033[m \033[1:32m para hexadecimal seria igual à"
          "\033[36m {}\033[m".format(num, hex(num)[2:]))
else:
    print("\033[31mNão exite esta opção.\033[m Tente novamente!")

