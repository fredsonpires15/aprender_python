
# Exercicio 1

# Faça um de tamanho 50 preechendo com o seguinte valor: (i+5*i)%(i+1), sendo i a 
#posição  do elemento no vetor. e em seguida imprima o vetor na tela.


""" lista = []
for valor in range(50+1):
    lista.append((valor+5*valor)%(valor+1))
    #print(valor,end=' ')

vetor = tuple(lista)
print(vetor)
print('os 5 primeiros elementos são:')
print(vetor[:6]) """

# Exercicio 2

""" Fazer um programa que receba do usuário dois vetores, A e B com 10
números inteiros cada. Em siguida crie um novo Vetor C ,calculando C = A-B. 
Mostre na tela os dados de C.
 """
 
""" from time import sleep
a = [2,3,46,7,8,9,14]
b = [3,5,1,8,13,15,27]
c = []
for ind , valor in enumerate(a):
    c.append(a[ind] + b[ind])
    
print(c)
    #print(i)
#print(c) """


# Exemplo 2

""" Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais 
que não são mútiplos de  7 ou que termina com 7.
 """
""" lista = []
for i in range(100):
    if i%7 != 0:
        lista.append(i)
print(lista)  """     
    

# Exercicio 3

""" faça um programa que calcula o desvio padrão de um vetor v contendo n = 10 
números onde m é a média do vetor
 """
v = [12,80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 96, 97, 99]
n = len(v)
media = sum(v)/ n

somatorio = 0
for ind , valor in enumerate(v):
    somar = (v[ind]-media)**2
    somatorio +=somar
variancia = (somatorio/ (n-1))
desvio_padrao = (somatorio/ (n-1))**(1/2)
desvio_padrao1 = pow((somatorio/ (n-1)),(1/2))
cv = (desvio_padrao/ media)*100
print(f'n={n}')
print(f'A média é : {media:.3f}')
print( f'O desvio padão é : {desvio_padrao:.3f}')
print(f'A variancia  é : {variancia:.3f}')
if cv <= 50:
    print(f'A Co-variancia é : {cv:.2f}% < 50%; logo, a média é uma medida representativa. ')
else: 
    print(f'A Co-variancia é : {cv:.2f}% < 50%; logo, a média não é uma medida representativa. ')


#print(desvio_padrao1)






    
       
