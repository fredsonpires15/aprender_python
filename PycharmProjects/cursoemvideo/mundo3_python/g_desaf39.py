
lista = ['Nanda','Sara','Edson']
linha = '»«'*30
for nome in lista:
    print(f'Olá {nome:>4} gostaria de jantar comigo hoje?')
print(linha)
print()
print(f'Tendo em conta que {lista[2]} não açeitou o convite, \nterei de fazer uma nova lista e convidar outras pessoas')
lista[2]= "Lea"
print()
print(linha)
#  nova lista de convidados
for nome in lista:
    print(f'Olá {nome:>4} gostaria de jantar comigo hoje?')
print(linha)
print()
print('No entanto, após chegar no restaurante, percebi que tinha muita comida \nSendo assim decide convidar mais três pessoas:')
lista.insert(0,"Ronilza")
lista.insert(2,'Gilberto')
lista.append('Luísa')
print()
print(linha)
for nome in lista:
    print(f'Olá  {nome}, gostaria de jantar comigo hoje?')

print(linha)
print()
print('agora só podem ficar duas pessoas!!')

lista.pop(0)
for nome in lista:
    print(f'Olá  {nome}, gostaria de jantar comigo hoje?')
print('Sinto muito, Roni, Já não será possivel te convidar para o jantar, peço imensa desculpa!!')
print(linha)  
print()

lista.pop(0)
for nome in lista:
    print(f'Olá  {nome}, gostaria de jantar comigo hoje?')
print('Sinto muito, Nanda, Já não será possivel te convidar para o jantar, peço imensa desculpa!!')
print(linha)
print()

lista.pop(0)
for nome in lista:
    print(f'Olá  {nome}, gostaria de jantar comigo hoje?')
print('Sinto muito, Gil, Já não será possivel te convidar para o jantar, peço imensa desculpa!!')
print(linha)
print()

lista.pop(0)
for nome in lista:
    print(f'Olá  {nome}, gostaria de jantar comigo hoje?')
print('Sinto muito, Sara, Já não será possivel te convidar para o jantar, peço imensa desculpa!!')
print(linha)

del lista[0]
del lista[0]
print(lista)
print(linha)
print()


