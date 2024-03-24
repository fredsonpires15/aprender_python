from calcular import Calcular

def main()-> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    print('==================0========00========00=========0===================')
    dificuldade: int = int(input('Informe o nível de dificuldade [1, 2, 3 ou 4]:  '))
    calc: Calcular = Calcular(dificuldade)
    
    print('----------------------------------------------------------------------------')
    print('\033[92mInforma o resultado da seguinte operação:\033[0m')
    calc.mostrar_operacao()

    resultado: int = int(input('Resposta: '))

    print('- - - - - - - - - - - - - - - - - - - - -  - - - - - -  - - - - - - -  - - ') 
    print()

    if calc.checar_resultado(resultado):
        pontos += 1
        print()

        print('»»«»»»«»»«»»«»«»«»«»»»»«»« Pontos »»»«»«»»«»«»»«»»«»«»««»»«»«»')
        print(f'             Você tem \033[31m {pontos} \033[0m ponto(s).')
        print('»»«»»»«»»«»«»«-------------------------------»»»«»«»««»»«»«»')
        print()

    continuar: int= int(input('Deseja contiuar no jogo [\033[32m 1 - Sim\033[0m , \033[31m  0 - Não\033[0m]: '))
    print()

    if continuar:
        jogar(pontos)
    else:
        print()
        print('\033[33m«»=«»=«»=«»=«»=«»=«»=«»=«»=«\033[0m \033[31m FINALIZADO \033[0m \033[33m «=«»=«»=«»=«»=»=«»=«»=«»=»=«»=«»  \033[0m')
        print(f'Parabens!! Você finalizou o jogo com {pontos} ponto(s).')
        print('até proxima!!')

        print()
        print()



if __name__ == '__main__':
    main()




