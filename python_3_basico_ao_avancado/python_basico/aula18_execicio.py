nome = "Fredson Pires"
tamanho_nome= len(nome)
nova_string = ''
indice = 0
while indice< tamanho_nome:
    letra = nome[indice]
    nova_string += letra + "*"
    
    indice += 1

print(nova_string)
    