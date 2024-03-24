from random import choices
n1 = str(input("Primeiro aluno:"))
n2 = str(input("Segundo aluno:"))
n3 = str(input("Terceiro aluno:"))
n4 = str(input("Quarto aluno:"))
lista = (n1, n2, n3, n4)
escolhido = choices(lista)
print("O aluno(a) escolhido(a) foi: {} ".format(choices(escolhido)))