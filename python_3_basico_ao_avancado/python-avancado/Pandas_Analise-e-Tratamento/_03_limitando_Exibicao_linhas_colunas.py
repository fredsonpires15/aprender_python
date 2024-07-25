import pandas as pd


# configurando o caminho do arquivo
vendas_DataFrame = pd.read_excel("C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Jan.xlsx")
 
#index - Exibir informações sobre quantidade de linhas que tem o DF
#print(vendas_DataFrame.index)

""" # Columns - Exibir informações sobre quantidade de colunas 
print(vendas_DataFrame.columns) """

""" #head - Exibir as 5 primeira linhas
print(vendas_DataFrame["Vendedor"].head()) """

""" #head - Exibir as primeira linhas determinadas
print(vendas_DataFrame.head(8)) """

""" #tail - Exibir as ultimas linhas
print(vendas_DataFrame.tail(3)) """

""" #Exibir as colunas que eu quero (Vendedor, Vendas)
print(vendas_DataFrame[["Vendedor", "Total Vendas"]].head(10)) """

""" # loc - Localizar e limitar linhas e colunas
print(vendas_DataFrame.loc[0: 4]) """

""" #loc - Pegar dados vendas do Leonardo Almeida
vendas_leornado = vendas_DataFrame.loc[vendas_DataFrame["Vendedor"]=="Leonardo Almeida"]
print(vendas_leornado) """

# pegar apenas vendedor e o total de vendas
vendas_leornado = vendas_DataFrame.loc[vendas_DataFrame["Vendedor"]=="Leonardo Almeida",["Vendedor", "Total Vendas"] ]
print(vendas_leornado)