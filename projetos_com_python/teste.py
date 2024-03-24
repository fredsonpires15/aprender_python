# pergunta 5
"""def somar_dois_menores(lista): 
    if len(lista) == 1:
        return lista[0]
    else:
        lis = list(lista)
        lis.sort()
        return lis[0] + lis[1]

lista = (["a","B"])
resultado = somar_dois_menores(lista)
print(resultado)"""

# pergunta 3
"""def pares_de_valores(x,y,z):
    lista = []
    for i in range(x, y+1):
        tupl = ((i,i**z))
        lista.append(tupl)
    return lista

print(pares_de_valores(0, 5, 2))"""

# pergunta 4
"""def multiplicar(tuplo):
    mult = 1
    while True:
        if tuplo == [] or ():
            return 0
        else:
            for i in tuplo:
                mult *= i
            return mult     

tuplo = []
print(multiplicar(tuplo))"""
 # pergunta 6
"""conjunto1 = [2, 5, 4]
conjunto2 = [87, 54, 2, 50, 7, 99, 42, 7, 8, 34, 35, 5, 47]
def e_subconjunto():
    conj = []
    for i in conjunto1:
        for j in conjunto2:
            if i == j:
                conj.append(j)
                
    return conj == conjunto1

print(e_subconjunto())"""
# pergunta 7
#def gerar_sequencia(inicio, passo,limite):
"""inicio = 10
passo = -1
limite = -1
lista = []

while inicio >= limite:
    inicio += passo
    print(inicio)"""

"""def ler_pontos(ficheiro):
    ler = open(ficheiro, "r")
    lista1 = ler.readline().strip().split(",")
    lista2 = ler.readline().strip().split(",")
    nova_lista1 = []
    nova_lista2 = []
    for i in range(len(lista1)):
        nova_lista1.append(float(lista1[i])) 
        nova_lista2.append(float(lista2[i]))
    ler.close()
    return nova_lista1, nova_lista2"""







  
# inicio = 0
# passo = 0.5
# limite = 5
#lista = gerar_sequencia(inicio, passo, limite)
#print(lista)

