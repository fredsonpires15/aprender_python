
import xlsxwriter as xw
import os


nomecaminhoArquivo = "C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\Banco_de_Dados.xlsx"

workbook = xw.Workbook(nomecaminhoArquivo)

sheetPadrao = workbook.add_worksheet()

sheetPadrao.write("A1", "Nome")
sheetPadrao.write("A2", "Fredson")
sheetPadrao.write("A3", "Edson")
sheetPadrao.write("B1", "Idade")
sheetPadrao.write("B2", "22")
sheetPadrao.write("B3", "24")
sheetPadrao.write("B4", "23")


workbook.close()

os.startfile(nomecaminhoArquivo)
""" a = 0
while True:

    a +=1
    print(f'A{a}')
    sair = input('Clique  [\033[92m enter\033[0m] para continuar ou [\033[91m s\033[0m] para sair: ')
    if sair.lower() == 's':
        break """



""" from cadastro_de_cliente import Cliente

if __name__ == '__main__':

    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    NIF = input('NIF: ')
    morada = input('Morada: ')
    codigo_postal = input('Código Postal: ')


    cadastro = Cliente(nome,sobrenome, NIF, morada, codigo_postal)
    cliente_1 = cadastro.cliente()

    print('|------------------------------------------------|')
    # print(f' {cadastro.nome()}')
    # print(f' {cadastro.nif()}')
    # print(f' {cadastro.morada()}')
    # print(f' {cadastro.codigo_postal()}')
    print(f'Informação do cliente: {cliente_1}')

    if nome in cliente_1['Nome']: 
        print('O cliente existe?' )
    else:
        ...
    print('|------------------------------------------------|') """


