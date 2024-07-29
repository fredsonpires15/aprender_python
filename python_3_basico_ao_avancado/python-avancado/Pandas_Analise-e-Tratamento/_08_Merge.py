
import pandas as pd


#Lendo os arquivos e tranformando em DataFrame
vendas_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Merge.xlsx')

vendedores_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendedores_Merge.xlsx')

produtos_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Produtos_Merge.xlsx')


# merge - une os DataFrames através de um denominador em comum
vendas_DF = vendas_DF.merge(vendedores_DF)
vendas_DF = vendas_DF.merge(produtos_DF)


resumo_DF = vendas_DF[['Vendedor','Produto','Total Vendas', 'Quantidade Vendida']]

print(vendas_DF)
print()
print()
print()
print(resumo_DF)
#print(vendedores_DF)
#print(produtos_DF)