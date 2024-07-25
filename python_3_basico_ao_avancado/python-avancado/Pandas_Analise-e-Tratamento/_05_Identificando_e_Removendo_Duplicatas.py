# Identificando e Removendo Duplicatas
import pandas as pd

baseVendas_DataFrame = pd.read_excel("C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\python_3_basico_ao_avancado\\python-avancado\\Pandas_Analise-e-Tratamento\\arquivos\\Base_Vendas.xlsx")


#nunique - Quantidade de valores unicos
valoresUnicos = baseVendas_DataFrame.nunique()

#subset - Colunas a serem verificadas
#keep - primeiro ou último e falso considera todos (keep=first, keep=last, keep=false)
#duplicated - Verificar se tem valores duplicados
verificarDuplicados = baseVendas_DataFrame.duplicated(subset="Vendedor", keep="first")

#criação de uma nova coluna para ver se tem valores duplicados
baseVendas_DataFrame["Valores Duplicado"] = baseVendas_DataFrame.duplicated(subset="Vendedor", keep="first")

# removendo valores duplicados
#drop_duplicates - remover valores duplicados
removerDuplicidade = baseVendas_DataFrame.drop_duplicates(subset="Vendedor", keep="first"  )

print(baseVendas_DataFrame)
#print(valoresUnicos)
print()
#print(verificarDuplicados)
print(removerDuplicidade)





