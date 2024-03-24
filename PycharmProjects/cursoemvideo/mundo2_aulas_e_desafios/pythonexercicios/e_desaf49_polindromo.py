frase = str(input("Digite uma frase:")).strip().upper()
palavra = frase.split()
junta = "".join(palavra)
inverso = junta[::-1]  # utilizando a tecnica de fatiamento
"""inverso = " "
for letra in range(len(junta) - 1, -1, -1):  
    inverso += junta[letra]"""
print("O inverso de \033[32m{} é \033[34m{}\033[m".format(junta, inverso))
if inverso == junta:
    print("Temos um\033[35m PALINDROMO.")
else:
    print("Não é um\033[31m PALINDROMO.")
