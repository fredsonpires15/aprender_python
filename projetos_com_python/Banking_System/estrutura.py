import os
import openpyxl
from openpyxl import workbook

def menu_login():
    print(f' |{"-"*42}|')
    print(f' |{" "*14}\033[1;90m Banco Gllasa\033[0;0m {" "*14}|')
    print(f' |{"-"*42}|')
    #print(f' |{"="*18} MENU {"="*18}|')
    print(' | [\033[1;36m 1 \033[0;0m] \033[1;31m Cadastrar Cliente\033[0;0m                 |')
    print(' | [\033[1;36m 2 \033[0;0m] \033[1;32m Login\033[0;0m                             |')
    print(f' |{"-"*42}|')  

    
def menu():
    print(f' |{"-"*42}|')
    print(f' |{" "*18}\033[1;90m MENU\033[0;0m {" "*18}|')
    print(f' |{"-"*42}|')
    #print(f' |{"="*18} MENU {"="*18}|')
    print(' |  [\033[1;36m 1 \033[0;0m] \033[1;32m Dados de Cliente \033[0;0m                |')
    print(' |  [\033[1;36m 2 \033[0;0m] \033[1;32m Depósitos \033[0;0m                       |')
    print(' |  [\033[1;36m 3 \033[0;0m] \033[1;32m Saques \033[0;0m                          |')
    print(' |  [\033[1;36m 4 \033[0;0m] \033[1;32m Transferências \033[0;0m                  |')                                  
    print(' |  [\033[1;36m 5 \033[0;0m] \033[1;32m Sair \033[0;0m                            |')                                  
    print(f' |{"-"*42}|')

def dados_cliente():
    print(' Mostrar Dados do usuário...')
    print(' ---identificação---------------------')
    print(' |                                   |')
    print(f'|                 Nome:             |')
    print(f'|                 Sexo:             |')
    print(f'|Identificação [PC/TR]:             |')
    print(f'|      Nºidentificação:             |')
    print(f'|     Data de validade:             |')
    print(f'|                  NIF:             |')
    print(f'|         Estado Civil:             |')
    print('-------------------------------------')
    print('')
    print('---Residência------------------------')
    print('|                                   |')
    print('|                 País:             |')
    print('|             Distrito:             |')
    print('|                  Rua:             |')
    print('|        Código-Postal:             |')
    print('-------------------------------------')
    print('')
    print('---Naturalidade----------------------')
    print('|                                   |')
    print('|     Data de Nascimento:           |')
    print('|                   País:           |')
    print('|               Distrito:           |')
    print('|                    Rua:           |')
    print('-------------------------------------')
    print('')
    print('---Contacto--------------------------')
    print('|                                   |')
    print('|              Telemóvel:           |')
    print('|                 E-mail:           |')
    print('-------------------------------------')
    depositar = input('Montante(€): ')
    os.system('cls')

book = openpyxl.load_workbook(filename= 'Projetos_com_python/Banking_System/Banco_de_Dados.xlsx')


nome = 'Fredson Vila Nova'
ws = workbook
banco_de_dados_page = book['Sheet1']
print(banco_de_dados_page["A3"].value)

for rows in banco_de_dados_page.iter_rows(min_row=2, max_row=3):
    for cell in rows:
        #print(f'{cell.coordinate} : {cell.value}')

        if nome in cell.value:
            print(cell.value)

    print()