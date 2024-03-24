"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta
  """
expressao = str(input('Digite a Expressão: '))

if expressao.count("(") == expressao.count(")"):
    print('A expressão está correta!!')
elif expressao.count("(") > expressao.count(")"):
    print('Expressão invalida!!')
    print('O "(" está á mais. Você deve fechar ou retirar o parênteses ')
else:
    print('Expressão invalida!!')
    print('O ")" está á mais. Você deve fechar ou retirar o parênteses')

