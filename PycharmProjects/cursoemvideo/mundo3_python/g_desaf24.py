""" Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno. 
 """

def area_do_terreno(largura, comprimento):
    area = largura*comprimento
    return f'A de um terreno de {largura}m x {comprimento}m é  de {area}m^2'


largura = float(input('Largura do terreno: '))
comprimento = float(input('Comprimento de terreno: '))
resultado = area_do_terreno(largura, comprimento)
print(resultado)

print()
print()
print()
