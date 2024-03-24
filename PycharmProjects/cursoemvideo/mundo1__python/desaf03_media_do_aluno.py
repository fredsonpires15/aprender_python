# ««««« Média do Aluno »»»»»
nome = input("por favor, diga o seu nome:")
port = int(input("Nota de Português:"))
mat = int(input("Nota de Matemática: "))
fis = int(input("Nota de física: "))
qui = int(input("Nota de química: "))
prog = int(input("Nota de programação:"))
media = (port + mat + fis + qui + prog)/5
print("O {} teve uma média  de  {:.0f} valores ".format(nome, media))
