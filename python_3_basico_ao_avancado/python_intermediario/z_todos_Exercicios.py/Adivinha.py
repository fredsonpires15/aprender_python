import random

def adivinha(tentativa):
    secreto = random.randint(0,100)
    for i in range(tentativa):
        numero = eval(input('O seu palpite: ')
                      )
        
        if numero == secreto:
            print('Uauu, acertou!!')
            return True
        elif numero >secreto:
            print('Muito grande...')
        else:
            print('MUito pequeno...')
    
    print('Lamento, mas esgotou as suas tentativas.')
    return False


adivinha(3)