import pandas as pd
import numpy as np


notas_alunos = pd.DataFrame({
    'Nome': ['Ana', 'Bia', 'Carlos', 'Daniel', 'Edu'],
    'Nota1': [9,5,7,12,17],
    'Nota2': [10,18, 12, 13, 19],
    'Nota3': [8, 15, 14, 16, 18],
    'Nota4': [10, 15, 14, 16, 17],

})

# Adicionando coluna e calculando a média
notas_alunos['Média'] = notas_alunos[['Nota1','Nota2','Nota3','Nota4']].mean(axis=1)

novacolunaFaltas = [2,3,0,2,0]
# Criando uma coluna com o valor padrão
notas_alunos['Faltas'] = novacolunaFaltas

#Localizar a linha 1 e alterar coluna (Nota2)
notas_alunos.loc[1, "Nota2"] = 18

# subistuir a coluna mèdia pela nova coluna média
notas_alunos['Média'] = notas_alunos[['Nota1','Nota2','Nota3','Nota4']].mean(axis=1)

print(notas_alunos)



