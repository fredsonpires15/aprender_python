import pandas as pd

""" 
#Lendo os arquivos e tranformando em DataFrame
loja1_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_+INNER_JOIN_LOja1.xlsx')

loja2_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_+INNER_JOIN_LOja2.xlsx')

#concat - Une os DataFrames loja1 e loja2
vendasLoja_1e2_DF = pd.concat([loja1_DF, loja2_DF])

semClienteDuplicado_DF = vendasLoja_1e2_DF.drop_duplicates(subset='Vendedor')


# print(loja1_DF)
# print()
# print(loja2_DF)
print()
print(vendasLoja_1e2_DF) 
print()
print(semClienteDuplicado_DF) """



#------------------------------------------------------------------------------------------------------#
#                                         Merge Left Join                                              #
#------------------------------------------------------------------------------------------------------#


"""  

vendas_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_LEFT_JOIN.xlsx')

vendedores_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendedores_LEFT_JOIN.xlsx')

#on - Qual coluna se refere ao denominador em comum
#how - Como as colunas se referem ao denominador em comum
#left - Esquerda
#merge - une os DataFrames através de um denominador em comum
#verificarVendas_DF = pd.merge(vendas_DF, vendedores_DF, on=['Id Vendedor'], how='left')

#suffixes = modar/renomear o nome da coluna
verificarVendas_DF = pd.merge(vendas_DF, vendedores_DF, on=['Id Vendedor'], how='left', suffixes=('_Vendas', '_Checagem'))

# limpar linhas vazias
limparlinhas_vazias = verificarVendas_DF.dropna()

# Deletar calunas de Vendedor checagem
del limparlinhas_vazias['Vendedor_Checagem']

# print(vendas_DF)
# print()
# print(vendedores_DF)
# print()
# print(verificarVendas_DF)
# print()
# print(limparlinhas_vazias)        """


#------------------------------------------------------------------------------------------------------#
#                                              Merge Outer                                             #
#------------------------------------------------------------------------------------------------------#

vendasLoja1_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Outer_Vendas_Loja1.xlsx')

vendasLoja2_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Outer_Vendas_Loja2.xlsx')

#merge - une os DataFrames através de um denominador em comum
verificarVendasLoja_DF = pd.merge(vendasLoja1_DF, vendasLoja2_DF, on=['Id Vendedor'], how='outer', suffixes=('Loja 1', 'Loja 2'))

#deletar linhas vazias
tratamentoDados_DF = verificarVendasLoja_DF.dropna()

# deletar coluna  VendedorLoja 2 
del tratamentoDados_DF['VendedorLoja 2']

tratamentoDados_DF['TotalVendas'] = tratamentoDados_DF['VendasLoja 1'] + tratamentoDados_DF['VendasLoja 2']

print(vendasLoja1_DF)
print()
print(vendasLoja2_DF)
print()
print(verificarVendasLoja_DF)
print()
print(tratamentoDados_DF)








