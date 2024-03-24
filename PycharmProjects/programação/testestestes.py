"""def id_citacao(autor, citacao):
    fra = autor + "  disse: " + citacao
    return fra


autor = "António"
citacao = "Programar é muito interessante!"
texto = id_citacao(autor, citacao)
print(texto)"""

"""def jar_jar():
    sequencia_ADN = 'TACTAC' + ('GATACAA' * 20 + 'CATCAT' * 10 + 'TA' * 8) * 40 + 'TACTAC'
    print(len(sequencia_ADN))
    return sequencia_ADN


jar_jar()"""

SEGUNDOS_POR_MINUTO = 60
MINUTOS_POR_HORA = 60


# Devolve o número de segundos, dado o número de minutos
def minutos_para_segundos(horas):
    return minutos * SEGUNDOS_POR_MINUTO


# Devolve o número de minutos, dado o número de horas
def horas_para_minutos(horas):
    return horas * MINUTOS_POR_HORA

    # Utilize as 2 funções anteriores (i.e., não utilize literais nem constantes)


def horas_para_segundos(horas):
    return horas_para_minutos(horas) * horas_para_segundos(horas)


# Aqui, apenas precisa de recorrer a 2 das 3 funcões anteriores (não utilize literais nem constantes)
def tempo_para_segundos(horas, minutos, segundos):
    return segundos + horas_para_segundos(horas) + horas_para_segundos(horas)


horas = 10
minutos = 30
segundos = 1
print(tempo_para_segundos(horas, minutos, segundos))
