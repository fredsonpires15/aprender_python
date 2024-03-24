""" Exercício Python 076: Crie um programa que tenha uma tupla
única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
 """

compras = ('Lapis', 1.2,
         'Borracha', 2.3,
         'Caneta', 12.032,
         'computador',200.343,
         'Teclado',30.889,
         'Telemóvel', 357.993,
         'Rato',10.778,
         'Auricular',4.599,
         'Curso',11.982,
         'Carregador', 3.5653)
print( ' ='*40)
print(f'   {"LITAGEM DE PREÇOS":^60}')
print(' ='*40)
for itens in range(0, len(compras)):
    if itens % 2 == 0:
        print(f'               {compras[itens]:.<30}', end='')
    else:
        print(f'   {compras[itens]:>7.2f} €')

print( ' ='*40)
print( ' ='*40)
