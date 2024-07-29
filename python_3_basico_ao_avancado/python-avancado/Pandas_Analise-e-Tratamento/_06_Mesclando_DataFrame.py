
#Mesclando DataFrame

import pandas as pd



#Lendo os arquivos e tranformando em DataFrame
vendasJaneiro_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Jan.xlsx')

vendasFevereiro_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Fev.xlsx')

vendasMarco_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Mar.xlsx')

#------------------------------------------------------------------------------------------------#
#                                      Mesclando DataFrame                                       #
#------------------------------------------------------------------------------------------------#
""" 
 #concat - Concatenando os DataFrames vendasJaneiro e vendasFevereiro
vendasGeral_DF =pd.concat([vendasJaneiro_DF, vendasFevereiro_DF, vendasMarco_DF]) 

#concat - Concatenando os DataFrames vendasJaneiro, vendasFevereiro e vendasMarco, e criando um novo DataFrame vendasGeralComGrupo_DF, usando o keys e o names para identificar os DataFrames 
vendasGeralComGrupo_DF = pd.concat([vendasJaneiro_DF, vendasFevereiro_DF, vendasMarco_DF], keys=['Janeiro', 'Fevereiro', 'Março'], names=['Mês'])

 #resumindo / pegando 3 colunas o DataFrame
resumindo_DF = vendasGeral_DF[["Vendedor","Data Venda", "Total Vendas" ]] 

#separando o mês de fevereiro

extrairFevereiro = vendasGeralComGrupo_DF.loc['Fevereiro']

#print(vendasGeral_DF)
print()
print(vendasGeralComGrupo_DF)
print()
print(extrairFevereiro)
#print(resumindo_DF)

# print(vendasJaneiro_DF)
# print(vendasFevereiro_DF)
# print(vendasMarco_DF) """
#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------#
#                                     Ordenação de dados                                         #
#------------------------------------------------------------------------------------------------#


#sort_values - ordena
#by - por qual coluna
# Ordenando o DataFrame vendasJaneiro_DF pelo nome do vendedor
ordenandoVendedor_DF = vendasJaneiro_DF.sort_values(by='Vendedor')


# Ordenando o DataFrame vendasJaneiro_DF pelo nome do produto
ordenandoProduto_DF = vendasJaneiro_DF.sort_values(by="Produto")

# Ordenar Duas colunas
ordenandoDuasColunas_DF = vendasJaneiro_DF.sort_values(by=["Vendedor","Produto"])

# Orderna do maior para o menor
# ascending = False - decrescente(do maior para o menor)
# ascending = True - crescente(do maior)
ordenando_ZaA_DF = vendasJaneiro_DF.sort_values(by='Vendedor', ascending=False)

#print(ordenandoVendedor_DF)
#print(ordenandoProduto_DF)
#print(ordenandoDuasColunas_DF)
print(ordenando_ZaA_DF)















