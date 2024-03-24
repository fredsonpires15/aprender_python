# texto = 'Python'
""" novo_texto = ''

for letra in texto:
    novo_texto+= f'*{letra}'
    print(letra)
print(novo_texto + '*') """

""" iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration: # StopIteration-> sinalixar para terminar a iteração
        break """

""" O for também fonciona com:
-continue
-braek
-else, etc """

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
    

    if i == 8:
        print('i é 8, seu else não executará')
        break
    for j in range(1,3):
        print(i,j)
else:
    print('For completo com secesso!')
    