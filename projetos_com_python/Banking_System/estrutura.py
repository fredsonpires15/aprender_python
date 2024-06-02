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
    ...
