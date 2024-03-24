l1 = int(input("Primeiro segmento:"))
l2 = int(input("Segundo segmento:"))
l3 = int(input("Terceiro segmento:"))
# if l2 + l3 > l1 == l2 == l3 < l1 + l2 and l2 < l1 + l3:  # será executado se todos os lados forem iguais
#   print("\033[1:32mPode formar um TRIANGULO equilátero")
# elif l1 < l2 + l3 and l2 == l3 or l2 == l1 or l1 == l3 and l2 < l1 + l3 and l3 < l1 + l2:
#   print("\033[1:32mPode formar um TRIANGULO isósceles ") # será executado se pelo menos dois lados forem iguais
# elif l2 + l3 > l1 != l3 != l2 != l1 and l2 < l1 + l3 and l3 < l1 + l2:
#   print("\033[1:32m Pode formar um TRIANGULO escaleno!!")  # será executado se todos forem diferentes
# else:
#   print("\033[1:31m Com esses lados não podes formar TRIANGULO!!")
if l2 + l3 > l1 and l2 < l1 + l3 and l3 < l1 + l3:
    if l1 == l2 == l3:
        print("\033[1:37mPode formar um triangulo\033[1:32m EQUILÁTERO!!")
    elif l1 != l2 != l3 != l1:
        print("\033[1:37mPode formar um triângulo \033[1:32mESCALENO!!")
    else:
        print("\033[1:37mPode formar um triângulo \033[1:32mISÓSCELES!!")
else:
    print("\033[1:31mNão podemos formar triângulo com esses dados\033[m."
          " \033[1:37mTente novamente com outros dados!!")