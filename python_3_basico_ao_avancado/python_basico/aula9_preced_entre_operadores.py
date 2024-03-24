# 1. (n + n) -> parênteses
# 2. ** -> exponenciação
# 3. *, //, /, % -> mult, divisão, div.inteira, resto.divisão
# 4. +,- -> adição, subtração
# o interpretador lê o codigo de esquerda para direita e 
# de cima para baixo

"""calcular o IMC de uma pessoa"""

nome = input("Seu nome:")
peso = float(input("Peso:"))
altura = float(input("Altura:"))
imc = peso / (altura**2)
print(f"{nome},o seu IMC é de:{imc:.2f}kg/m2")