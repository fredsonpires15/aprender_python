"""um programa que lê o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
soma = 0
mediaidade = 0
totmulher20 = 0
maioridadehomem = 0
nomevelho = ""
for c in range(1, 5):
    print("»«»»«»«»»««» {}ªPESSOA «»«»«»«»«»»« ".format(c))
    nome = str(input("Nome:"))
    idade = int(input("Idade:"))
    sexo = str(input("sexo [M/F]:"))
    print("..............................")
    soma += idade
    if c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
media = soma / 4

print("A média de idade é {}".format(media))
print("O homem mais velho tem {} anos e se chama: {} ".format(maioridadehomem, nomevelho))
print("Tivemos pelo menos {} mulheres com menos de 20 anos".format(totmulher20))