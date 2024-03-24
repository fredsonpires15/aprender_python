from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    """ uma classe para gerar passeios aleatorios."""

    def __init__(self, num_points=5000):  # inicializar os pontos atribuidos de um passeio
        self.num_points = num_points

        # todos os passeios começam em (0,0)
        self.x_valor = [0]
        self.y_valor = [0]

    def fill_wilk(self):  # calcular todos os pontos do passeio.
        # continuar dando os passos até que o passeio alcance o tamanho desejado
        while len(self.x_valor) < self.num_points:
            # direção a ser  seguida e distância a ser percorrida nessa direção
            direcao_x = choice([1, -1])
            distancia_x = choice([0, 1, 2, 3, 4])
            passo_x = direcao_x * distancia_x
            direcao_y = choice([1, -1])
            distancia_y = choice([0, 1, 2, 3, 4])
            passo_y = distancia_y * direcao_y

            # rejeitar movimentos que não vão a lugar nenhum

            if passo_x == 0 and passo_y == 0:
                continue

            # calcular os proximos valores de X e Y

            proximo_x = self.x_valor[-1] + passo_x
            proximo_y = self.y_valor[-1] + passo_y

            self.x_valor.append(proximo_x)
            self.y_valor.append(proximo_y)


rw = RandomWalk()
rw.fill_wilk()
plt.scatter(rw.x_valor, rw.y_valor, s=15)
plt.show()
