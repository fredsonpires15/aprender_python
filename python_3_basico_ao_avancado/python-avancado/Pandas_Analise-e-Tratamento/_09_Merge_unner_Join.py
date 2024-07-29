import pandas as pd


#Lendo os arquivos e tranformando em DataFrame
Vendas_LOja1 = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_+INNER_JOIN_LOja1.xlsx')

Vendas_LOja2 = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_+INNER_JOIN_LOja2.xlsx')



# merge - une os DataFrames através de um denominador em comum

#on - Qual coluna se refere ao denominador em comum
#how - Como as colunas se referem ao denominador em comum
#inner - Seleciona apenas os registros que se referem ao denominador em comum

#procurar e exibir os vendedores que tem vendas em ambas as lojas
vendedoresAmbos_DF = pd.merge(Vendas_LOja1, Vendas_LOja2, on=['Vendedor'], how='inner')

#suffixes = modar o nme da coluna
vendedoresAmbosResumo_DF = pd.merge(Vendas_LOja1, Vendas_LOja2[["Vendedor", "Total Vendas"]], on=['Vendedor'], how='inner', suffixes=('LOJA 1', 'LOJA 2'))

#
resumo = vendedoresAmbosResumo_DF[['Vendedor','Total VendasLOJA 1', 'Total VendasLOJA 2']]
#print(Vendas_LOja1)
print()
#print(Vendas_LOja2)
print()
#print(vendedoresAmbos_DF)
print()
print(vendedoresAmbosResumo_DF)
print()
print(resumo)

#print(vendedores_DF)
#print(produtos_DF)