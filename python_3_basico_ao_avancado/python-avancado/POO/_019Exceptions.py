# Criando Exceções em Python Orientado a Objetos
# Para criar uma exceção em Python, você só
# precisa herdar alguma exceção da linguagem.
# A recomendação do documento é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando abordagens (com colocar Error ao final)
# Levantando (raise) / Lançando (throw) abordagens
# Relançando abordagens
# Adicionando notas em abordagens (3.11.0)


class MeuError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'd', 'oi')
    exception_.add_note('É apenas uma teste')
    exception_.add_note('É apenas uma teste')
    raise exception_

try:
    levantar()

except MeuError as error:
    print(error.__class__.__name__)
    print(error.args)






































