"""def obter_fraccao(num, den):
    x = max(num, den)
    y = len(str(x))
    print(num)
    print("-" * y)
    print(den)

obter_fraccao(12, 13)"""

"""
def linha():
    print("-" * 30)


print(
    " [1] - Carregar ficheiro \n [2] - Listar tudo \n [3] - Listar nota do aluno \n [4] - Comparar alunos \n [5] - Gerar CSV processado \n [X] - Sair  ")

opcao = int(input("Introduza sua opção:")) or "x"
if opcao == 1:
    linha()
    print("Carregar ficheiro")
    linha()
elif opcao == 2:
    linha()
    print("Listar tudo")
    linha()
elif opcao == 3:
    linha()
    print("Listar nota do aluno")
    linha()
elif opcao == 4:
    linha()
    print("Comparar alunos")
    linha()
elif opcao == 5:
    linha()
    print("Gerar CSV processado")
    linha()
elif opcao > 5:
    print('Opção inválida!!')
elif opcao == "x":
    print()"""

# noinspection PyUnreachableCode
"""def my_abs(n):
    if n == 0:
        print("iu")


my_abs(-4)"""

"""def obter_numero_dia(dia):
    if dia == "Domingo" or "domingo":
        if dia == "Domingo" or "domingo":
            return "1º"
        else:
            return "N/A"
    elif dia == "Segunda" or "segunda":
        if dia == "Segunda" or "segunda":
            return "2º"
        else:
            return "N/A"
    elif dia == "Terça" or "terça":
        if dia == "Terça" or "terça":
            return "3º"
        else:
            return "N/A"
    elif dia == "Quarta" or "quarta":
        if dia == "Quarta" or "quarta":
            return "4º"
        else:
            return "N/A"
    elif dia == "Quinta" or "quinta":
        if dia == "Quinta" or "quinta":
            return "5º"
        else:
            return "N/A"

    elif dia == "Sexta" or "sexta":
        if dia == "Sexta" or "sexta":
            return "6º"
        else:
            return "N/A"

    elif dia == "Sabádo" or "sabádo":
        if dia == "Sabádo" or "sabádo":
            return "7º"
        else:
            return "N/A"


obter_numero_dia("segund")"""
from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

dado1 = imread("dice1.png", as_gray=True)
plt.imshow(dado1, cmap=cm.gray)
plt.show()