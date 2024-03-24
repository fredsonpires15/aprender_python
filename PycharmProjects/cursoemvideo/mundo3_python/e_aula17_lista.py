""" num = [1,2,4,5,8,2,6,8,9,2]
num.append(9)
num.sort(reverse=False)
num.insert(3,2)
if 2 in num:
    num.remove(2)
    print(num)
else:
    print('Não achei a nº 2')
print(num) """
valores = []
for i in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for indice, cont in enumerate(valores):
    print(f'Na posição {indice + 1} encontrei o valor {cont}') 

print('E chegei ao final desta lista')
