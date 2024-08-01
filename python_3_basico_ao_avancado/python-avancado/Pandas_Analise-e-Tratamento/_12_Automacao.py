import pandas as pd
import xlsxwriter

#Lendo os arquivos e tranformando em DataFrame

baseDados_DF = pd.read_excel('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Vendas_Jan.xlsx')

# remover valores duplicados
#subset= colunas que serão verificadas, keep='first'
removerDuplidados_DF = baseDados_DF.drop_duplicates(subset='Vendedor', keep='first')

for linha in removerDuplidados_DF['Vendedor']:
    
    #loc - Localizar e limitar linhas
    #vendasFuncionario = baseDados_DF.loc[baseDados_DF['Vendedor'] == linha]
    vendasFuncionario = baseDados_DF.loc[baseDados_DF['Vendedor'] == 'Leonardo Almeida']
    #vendasFuncionario = baseDados_DF.loc[baseDados_DF['Vendedor'] == linha]


    # Guardar os dados em arquivo Excel em massa
    guardar_arquivo_excel = pd.ExcelWriter('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\relatorio\\Relatorio Vendas' + linha + '.xlsx', engine="xlsxwriter")

    # Guardar os dados em arquivo Excel
    guardar_arquivo_excel = pd.ExcelWriter('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\relatorio\\Relatorio Vendas' + 'Leonardo Almeida' + '.xlsx', engine="xlsxwriter")
    guardar_arquivo_excel.close()

    #transformar os dadso em DataFrame
    dataFrame = pd.DataFrame(vendasFuncionario)

    
    #preparar o arquivo excel em massa
    #guardar_arquivo_excel = pd.ExcelWriter('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\relatorio\\Relatorio Vendas' + linha + '.xlsx', engine="xlsxwriter")

    #preparar o arquivo excel
    guardar_arquivo_excel = pd.ExcelWriter('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\relatorio\\Relatorio Vendas' + 'Leonardo Almeida' + '.xlsx', engine="xlsxwriter")

    # Escrever o DataFrame no arquivo Excel
    dataFrame.to_excel(guardar_arquivo_excel, sheet_name='Vendas', index=False)

    #Salvar as alterações
    guardar_arquivo_excel.close()

print('Arquivo gerado com sucesso!')


# Guardar os dados em arquivo CSV
#vendasFuncionario.to_csv('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\relatorio\\Relatorio Vendas' + 'Leonardo Almeida' + '.csv')






#print(baseDados_DF)
print('Relatorio gerado com sucesso!')
#print(removerDuplidados_DF)
