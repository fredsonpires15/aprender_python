# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
print(duplicar(2))
print(duplicar(3))
print(triplicar(5))
print(triplicar(6))
print(quadruplicar(7))
print(quadruplicar(8))
print(quadruplicar(9))