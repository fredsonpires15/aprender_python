def saudacao(msg, nome):
        return f'{msg}, {nome}'


def executa(funcao, *args):
        return funcao(*args)

print(executa(saudacao, 'boma dia', 'Luiz'))
print(executa(saudacao, 'boma dia', 'Joel'))
print(executa(saudacao, 'boma dia', 'Ana'))