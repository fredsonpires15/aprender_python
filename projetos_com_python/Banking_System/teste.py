import openpyxl

# Carregar o arquivo Excel
arquivo = "C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\Banco_de_Dados.xlsx"
# Carregar o arquivo Excel
workbook = openpyxl.load_workbook(arquivo)

# Selecionar a planilha desejada
sheet_selecionada = workbook.active

# Definir a função de comparação
def cliente_corresponde(nome, nif):
    return nome == 'Fredson Vila Nova' and int(nif) == 308806662

# Percorrer cada linha na planilha, começando na linha 2 para ignorar o cabeçalho
nome_encontrado = False
for row in range(2, sheet_selecionada.max_row + 1):
    name_cell = sheet_selecionada.cell(row=row, column=1).value  # Coluna "A" para os nomes
    nif_cell = sheet_selecionada.cell(row=row, column=8).value   # Coluna "H" para os NIFs

    if cliente_corresponde(name_cell, nif_cell):
        nome_encontrado = True
        break

if nome_encontrado:
    print("O nome 'Fredson Vila Nova' está presente no banco de dados.")
else:
    print("O nome 'Fredson Vila Nova' não está presente no banco de dados.")