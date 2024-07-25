import pandas as pd


# configurando / abrindo o arquivo
dataFramedados = pd.read_excel("C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Deletar_Linhas_Colunas.xlsx")


# dropna - deletando linhas que tem pelo menos um valor em branco
deletandoLinhasEmBranco = dataFramedados.dropna()

""" #del - Deleta a coluna que especificarmos
del deletandoLinhasEmBranco['Produto'] """

#drop - Deletando duas ou mais colunas
deletarduascolunas = deletandoLinhasEmBranco.drop(columns=['Produto', 'Data Venda'])

#drop - Deletando linhas 
excluirLinha3 = deletarduascolunas.drop(2, axis=0)
excluirLinha3 = excluirLinha3.drop([0,1])
print(excluirLinha3) 












