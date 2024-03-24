print("\033[1:32m-=" * 20)
print("       \033[7:37m ANALISADOR DE TRIÂNGULOS \033[m   ")
print("\033[1:32m-=\033[m" * 20)
l1 = float(input("primeiro segmento:"))
l2 = float(input("segundo segmento:"))
l3 = float(input("Terceiro segmento:"))
if l1 < l3 + l2 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Pode formar um \033[7:33mTRIÂNGULO!\033[m")
else:
    print("Nâo pode formar um \033[7:33mTRIÂNGULO\033[m")

