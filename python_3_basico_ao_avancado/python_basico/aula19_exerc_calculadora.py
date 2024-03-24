"""Calculadora com While"""
menu = 'Menu'

while True:
    print()
    print("«»«»"*10)

    print(f'{menu:.^20}')
    print('[1] -> Adição\n'
        
          '[2] -> Subtração\n'
          '[3] -> Multiplicação\n'
          '[4] -> Divisão\n'
          '[5] -> Divisão inteira\n'
          '[6] -> Resto da Divisão\n'
          '[7] -> Sair'
          ) 
    print("«»«»"*10)
    
    op = int(input("sua Opção: "))
    if op not in [1,2,3,4,5,6,7]:
        print('Opção inválida. Tente Novamente!!')
        continue

    if op == 7:
        break

    num1 = (input('Digite o primeiro número:'))
    num2 = (input('Digite o segundo número:'))


    num1_float = 0
    num2_float = 0
    numeros_validos = None 


    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
        
        
    except:
        numeros_validos = None 
    
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invalidos.')
        continue

    print(" ")
    print("Realinzando sua conta. Confira o resultado abaixo: ")
    print(" ")

    
    if op == 1:
        somar = num1_float + num2_float
        print(f'   {num1_float} + {num2_float} = {somar}')
    elif op == 2:
        if num1_float > num2_float:
            sub = num1_float - num2_float
        else:
            sub = num2_float - num1_float
        print(f'  {num1_float} - {num2_float} = {sub}')
    elif op == 3:
        mul = num1_float * num2_float
        print(f'  {num1_float} * {num2_float} = {mul}')
    elif op == 4:
        div = num1_float / num2_float
        print(f'  {num1_float} / {num2_float} = {div}')
    elif op == 5:
        div_int = num1_float // num2_float 
        print(f'  {num1_float} // {num2_float} = {div_int}')
    elif op == 6:
        resto = num1_float % num1_float 
        print(f' {num1_float} % {num2_float} = {resto}')

    

    
    