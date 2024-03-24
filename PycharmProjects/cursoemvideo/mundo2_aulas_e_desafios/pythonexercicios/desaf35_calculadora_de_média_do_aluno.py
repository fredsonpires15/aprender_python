n1 = float(input("primeira nota:"))
n2 = float(input("Segunda nota:"))
media = (n1 + n2) / 2
print("\033[1:37mA média entre {:.1f} e {:.1f} é igual a {:.1f} ".format(n1, n2, media))
if media < 10:
    print("\033[1:31m O aluno está Reprovado!! \033[m")
elif 10 <= media < 14:
    print("\033[1:32m O aluno está em Recuperação!! ")
elif media >= 14:
    print("\033[1:34m O aluno foi Aprovado!!")
