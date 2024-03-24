"""um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores
 e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores."""
per = "Ss"
num = media = soma = quantidade = 0
maior = menor = 0
while per in "Ss":
    num = int(input("Digite um número inteiro:"))
    quantidade += 1
    soma += num
    per = str(input("Quer continuar? [Ss/Nn]"))
    media = soma / quantidade
    if quantidade == 1:
        maior = num
        menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

print("você digitou {} números e a soma é {}\n E a média é de {}".format(quantidade, soma, media))
print("O maior número é {} e o menor é {}".format(maior, menor))
