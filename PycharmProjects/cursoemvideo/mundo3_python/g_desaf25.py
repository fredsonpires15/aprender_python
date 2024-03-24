""" Faça um programa que tenha uma função chamada write(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
Ex: write('Olá, Mundo!') Saída:      
~~~~~~~~~ # Hello world
Olá, Mundo!
~~~~~~~~~ """

""" def write(object):
    symbol = '~'*(len(object)+2)
    return f'{symbol}\n {object}\n{symbol}'


reply1 = write('Fredson pires Vila Nova')
reply2 = write("I'm fredson pires Vila Nova, son of Fernanda Rosa Pires Damião")
print(reply1)
print(reply2) """ 

# the  soluctoin given(dada) by  ChatGPT
def create_border(symbol, length): # criar borda de com '~'
    return symbol * length

# function  to write
def write(string):
    symbol = '~'
    border_length = len(string) + 4  # Acrescenta 2 símbolos em cada extremidade
    border = create_border(symbol, border_length)
    return f"{border}\n  {string}\n{border}"

reply1 = write('Fredson pires Vila Nova')
reply2 = write("I'm Fredson Pires Vila Nova, son of Fernanda Rosa Pires Damião")
print(reply1)
print(reply2)
