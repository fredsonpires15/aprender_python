import pandas as pd
import numpy as np

""" #periods = quantos dias
#20231001 = Ano/ Mês / dia
dataFrame_Datas = pd.date_range('20231001', periods=11)
print(dataFrame_Datas) """

""" numeros_aleatorios = pd.DataFrame(np.random.rand(5,4)*10)

print(numeros_aleatorios) """

pessoa = {'Nome': ['João', 'Maria', 'Pedro'],
          'Idade':[25,24,21],
          'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
          }

df = pd.DataFrame(pessoa)

print(df)