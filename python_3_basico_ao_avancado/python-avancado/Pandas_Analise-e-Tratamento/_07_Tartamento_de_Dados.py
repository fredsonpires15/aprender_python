import pandas as pd


dados_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Tratamento_Dados.xlsx')
#print(dados_DF)

#fillna - Substituir valores vazios por media
#dados_DF["Total Vendas"] = dados_DF['Total Vendas'].fillna(dados_DF['Total Vendas'].mean())


#fillna - Substituir valores vazios com um valor padrão
#dados_DF["Total Vendas"] = dados_DF['Total Vendas'].fillna(2)


#ffill - Substituir valores vazios por ultimos valores anteriores validos
dados_DF["Total Vendas"] = dados_DF['Total Vendas'].ffill()


print(dados_DF)