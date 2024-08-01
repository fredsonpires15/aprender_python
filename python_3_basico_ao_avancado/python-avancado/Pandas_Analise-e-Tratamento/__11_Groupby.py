import pandas as pd

#Lendo os arquivos e tranformando em DataFrame
vendas_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Groupby.xlsx')


#mediavendedor_DF = vendas_DF.groupby(['Vendedor']).sum()

# Calculate the mean of the 'Vendedor' column after filtering out non-numeric values
vendas_DF["Total Vendas"] = vendas_DF["Preço"] * vendas_DF["Qtd"]
#mediavendedor_DF = vendas_DF.groupby(['Vendedor']).agg({'Total Vendas': 'sum', 'Qtd': 'sum'})
mediaVendedor = vendas_DF.groupby(["Vendedor","Produto"])["Total Vendas"].mean()

#sumVendedor = vendas_DF.groupby(['Vendedor']).sum()

#print(mediavendedor_DF)

#print(vendas_DF)
#print()
#print(mediavendedor_DF)
print()
#print(mediaVendedor)

#---------------------------------------------------------------------------------------------------#
#                                              pivot                                                #
#---------------------------------------------------------------------------------------------------#
#não podemos usar o pivot com dados repitidos
vendasPivot_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Lanchonete_Pivot.xlsx')


pivotExemplo = vendasPivot_DF.pivot(index="Data Venda", columns="Cliente", values="Preço com Desconto")
#print(pivotExemplo)


#---------------------------------------------------------------------------------------------------#
#                                        pivot_table                                                #
#---------------------------------------------------------------------------------------------------#

vendasPivot_Table_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Lanchonete_Pivot_Table.xlsx')


#pivotExemplo1_DF  = vendasPivot_Table_DF.pivot_table(index="Data Venda", columns="Cliente", values="Preço com Desconto", aggfunc="sum")

pivotExemplo2_DF  = vendasPivot_Table_DF.pivot_table(index="Data Venda", columns="Cliente", values=["Preço Total","Preço com Desconto"],aggfunc="sum" )

pivotExemplo3_DF  = vendasPivot_Table_DF.pivot_table(index="Data Venda", columns="Cliente", values="Preço com Desconto", aggfunc="sum")

pivotExemplo2_DF["Preço com Desconto"] = pivotExemplo2_DF["Preço com Desconto"].fillna(0)
pivotExemplo2_DF["Preço Total"] = pivotExemplo2_DF["Preço Total"].fillna(0)

#print(vendasPivot_Table_DF)
print()
print()
print(pivotExemplo2_DF)






