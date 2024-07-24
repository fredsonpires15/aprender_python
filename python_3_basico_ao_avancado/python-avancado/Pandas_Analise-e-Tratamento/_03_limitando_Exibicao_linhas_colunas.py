import pandas as pd


# configurando o caminho do arquivo
vendas_DataFrame = pd.read_excel("C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Jan.xlsx")

#index - Exibir informações sobre quantidade de linhas que tem o DF
print(vendas_DataFrame.index)

# Columns - Exibir informações sobre quantidade de colunas 
print(vendas_DataFrame.columns)

#head - Exibir as 5 primeira linhas
#print(vendas_DataFrame["Vendedor"].head())

#head - Exibir as primeira linhas determinadas
print(vendas_DataFrame.head(8))

#tail - Exibir as ultimas linhas



