from random import randint

""" 
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o nível de
dificuldade do jogo e após isso gera e apresenta, de forma aletaória, um cálculo para que possamos
informar o resultado.
Iremos limitar as operações em somar, diminuir e multiplicar. Se o usuário acertar a resposta, somará 1 ponto ao seu score.
Acertando ou errando, ele poderá ou não continuar o jogo.

"""

class Calcular:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1-> somar; 2->subtrair; 3-> multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade
        
    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao
    
    @property
    def resultado(self: object) -> int:
        return self._gerar_resultado



    def __str__(self) -> str:

        op: str = ' '
        if self.operacao == 1:
            op = 'somar. . .'

        elif self.operacao == 2:
            op = 'subtrair. . .'

        elif self.operacao == 3:
            op = 'multiplicar. . .'

        else:
            op = 'Não existe esta operação'

        return f'Valor1:{self.valor1}\n Valor2:{self.valor2} \n dificudade:{self.dificuldade} \n Operação:{op} \n resultado: {self._gerar_resultado}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1,10)
        
        elif self.dificuldade == 2:
            return randint(1, 100)
        
        elif self.dificuldade == 3:
            return randint(1, 200)
        
        elif self.dificuldade == 4:
            return randint(1, 500)
        
        else:
            return randint(1, 1000)
        
    @property
    def _gerar_resultado(self: object) -> int:

        if self.operacao == 1:
            return self.valor1 + self.valor2
        
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        
        elif self.operacao == 3:
            return self.valor1 * self.valor2
    @property   
    def _op_simbolo(self: object) ->str:
        if self.operacao == 1:
            return '+'
        
        if self.operacao == 2:
            return '-'
        
        if  self.operacao == 3:
            return '*'


    def checar_resultado(self: object, resposta: int) ->int:

        correto: bool = False

        if self.resultado == resposta:
            print('\033[33m Resposta correta \033[0m')
            correto = True

        else:
            print('\033[31m Resposta Errada!! \033[0m')

        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')

        return correto 
        
    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = \033[31m? \033[0m')


