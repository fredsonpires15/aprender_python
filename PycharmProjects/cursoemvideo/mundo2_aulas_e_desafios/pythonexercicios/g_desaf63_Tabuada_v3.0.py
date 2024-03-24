"""Faça um programa que mostre a tabuada de vários números,
 um de cada vez, para cada valor digitado pelo usuário.
  O programa será interrompido quando o número solicitado for negativo."""

print('\033[33m=-'*16)
print(' \033[31m         TABUADA  \033[m           ')
print('\033[33m=-\033[m'*16)


while True:
    print('__' * 18)
    tab = int(input('Quer ver a tabuada de quanto?'))

    print('__' * 18)
    print(':-' * 8
          )
    for n in range(1, 11):
        res = tab * n
        print(f'{tab} x {n} = {res}')
    print(':-' * 8)
    op = str(input('Clicar \033[41:30:1m[X]\033[m- para encerrar... '
                   ' \033[42:30:1m[C]\033[m - para marcar um outro valor:'))
    if op == 'x':
        break
print('\033[31mPROGRAMA ENCERRADO COM SUCESSO!!')