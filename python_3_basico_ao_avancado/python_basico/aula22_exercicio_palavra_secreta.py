"""Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário."""
import os 
from random import choice

palavra = choice(('perfume','amor','honestidade', 'verdade',
                'respeito','liberdade','perdão','esperança',
                'paz','plenitude','autenticidade','sorriso',
                'gratidão',    'reciprocidade',     'arte'))
letras_acertada = ''
tentativas = 0
while True:
    tentativas += 1
    letra = input('\nDigite uma uma letra:')
    if len(letra) > 1:
        print("Por favor, digite apenas uma letra.")
        continue

    if letra in palavra:
        letras_acertada += letra


    palavra_formada = ''

    for letra_secreta in palavra:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('palavra formada:',palavra_formada)
    if palavra_formada == palavra:
        os.system('cls')
        print('PARABENS, VOCÊ ACERTOU!!')
        print('A palavra secreta é:',palavra)
        print('Tentativas:',tentativas)
        palavra = ''
        tentativas = 0
        op = input('Quer continuar? sim-[s] ou não-[n]').lower()
        if op == 'n':
            break

