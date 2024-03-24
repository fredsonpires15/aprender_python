"""Calculadora com While"""
menu = 'Menu'

while True:
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    print(f'{menu:.^20}')
    print('[1] -> Adição\n'

          '[2] -> Subtração\n'
          '[3] -> Multiplicação\n'
          '[4] -> Divisão\n'
          '[5] -> Divisão inteira\n'
          '[6] -> Resto da Divisão\n'
          '[7] -> Sair'
          )

    op = int(input("sua Opção: "))
    if op == 1:
        somar = num1 + num2
        print(f'A soma entre {num1} e {num2} é {somar}')
    elif op == 2:
        if num1 > num2:
            sub = num1 - num2
        else:
            sub = num2 - num1
        print(f'A subtração entre {num1} e {num2} é {sub}')
    elif op == 3:
        mul = num1 * num2
        print(f'A soma entre {num1} e {num2} é {mul}')
    elif op == 4:
        div = num1 / num2
        print(f'A soma entre {num1} e {num2} é {div}')
    elif op == 5:
        div_int = num1 // num2
        print(f'A soma entre {num1} e {num2} é {div_int}')
    elif op == 6:
        resto = num1 % num1
        print(f'A soma entre {num1} e {num2} é {resto}')
    elif op == 7:
        break
