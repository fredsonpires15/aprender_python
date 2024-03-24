"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""


"""cont = num = soma = 0
while num != 999:
    num = int(input("Digite um número inteiro [999 para parar:"))
    soma += num
    cont += 1
print("Acabou!!")
print("Você digitou {} números e a soma é {}".format(cont - 1, soma - 999))"""

# outro forma de resolver

num = 0
cont = 0
soma = 0
num = int(input("Digite um número inteiro [999 para parar:"))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número inteiro [999 para parar:"))
print("Acabou!!")
print("Você digitou {} número e a soma é {}".format(cont, soma))

