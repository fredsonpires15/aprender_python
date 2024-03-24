""" Melhore o DESAFIO 61, perguntando\n para o usuário se ele
quer mostrar mais alguns termos. O programa encerrará quando
ele disser que quer mostrar 0 termos."""
print('\033[33m=«»\033[m' * 5)
termo: int = int(input("Primeiro termo:"))
razao = int(input("Razão:"))
cont = 6
total = 2
mais = 1
while mais != 0:
    total = total + mais
    while cont <= total:
        pA = termo + (cont - 1) * razao
        print("\033[33:1m{}".format(pA), end=" \033[31:1m-> \033[m")
        cont += 1
    print("\033[31m Em pausa!!\033[m")
    mais = int(input("QUer mostrar mais quantos termos?"))
print("FIM!!")
print("Ao todo foram mostrados {} termos".format(total))

