"""Crie um programa que leia dois valores e mostre um menu na tela:
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep

n1 = int(input("\033[33mDigite o primeiro valor:"))
n2 = int(input("\033[33mDigite um segundo valor:"))
op = 0
while op != 5:
    print("""\033[34mEscolha uma opção no seu menu:
    \033[31m[1] - \033[mSomar
    \033[32m[2] - \033[mMultiplicar
    \033[33m[3] - \033[mMaior
    \033[34m[4] - \033[mNovos números
    \033[35m[5] - \033[mSair do programa""")
    op = int(input("\033[36mSua opção:"))
    if op == 1:
        soma = n1 + n2
        print("\033[39mA soma entre \033[35m{}\033[m + \033[35m{}\033[m é \033[35m{}\033[m".format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print("\033[33mA produto entre \033[35m{} x {} \033[33mé\033[m {}".format(n1, n2, mult))
    elif op == 3:
        if n1 < n2:
            print("\033[34mO maior valor é \033[33m{}".format(n2))
        elif n1 > n2:
            print("\033[34mO maior valor é \033[33m{}".format(n1))
        elif n1 == n2:
            print("\033[32mAmbos são iguais.")
    elif op == 4:
        print("\033[36mInforme novos valores")
        n1 = int(input("\033[36mPrimeiro valor:"))
        n2 = int(input("Segundo valor:"))
    elif op == 5:
        print("\033[36mFinalizando o programa.....")
        sleep(2)
    else:
        print("\033[31mOpção Inválida. \033[36mTente novamente!!")
    print("\033[1:39m»=«"*11)
    print("\033[1:39m»=«" * 11)
print("\033[37mFIM do programa!!\033[m")
