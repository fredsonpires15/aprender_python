
import xlsxwriter as xw 
import os
from time import sleep

from cadastro_de_cliente import Cliente, CadastrarCliente
from colorama import Fore, Back, Style
from validar import validar_senha_usuario
from estrutura import menu_login, menu, dados_cliente
from Coletar_Dados import ColetarDados




def main():

    arquivo = "C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\Banco_de_Dados.xlsx"
    arquivo_senha = "C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\senha.xlsx"


    nome_valido = 'Fredson'
    senha_valida = '123'
    
    listar_clientes = []  # Lista para armazenar os clientes registrados

    while True:
        print()
        menu_login() # fazer login ou cadastro
        op = int(input('Opção: ') )
        print()
        print()
        print()
        os.system('cls')
        
        #print(Cliente.coletar_dados_Client().validar_cliente())

        if op == 1:  
            novo_cliente = ColetarDados()
            
            cliente = novo_cliente.dados_do_cliente(arquivo)

            
            #if isinstance(cliente, bool):
                 #...

            if cliente is None:
                os.system('cls')
                print()
                print()
                print('\033[91m O Cliente já foi registrado!\033[0m')
                

            else:
                print()
                cliente.banco_de_dados(arquivo)
                novo_cliente.regitar_client(arquivo_senha)
                
            
            sleep(7)
            os.system('cls')
            


        elif op == 2:
                nome = input('Nome do usúario: ')
                senha = input('Senha: ')
                os.system('cls')

                if  validar_senha_usuario(nome,senha, nome_valido, senha_valida):
                        while True:
        
                            menu()
                            op = int(input('Opção: ') )
                            print()
                            print()
                            os.system('cls')

                            if op == 1:
                                print(' Realizar um deposito...')
                                depositar = input('Montante(€): ')
                                dados_cliente()
                            elif op == 2:
                                print(' Sacar dinheiro na conta...')
                                sacar = input('Montante(€): ')
                                os.system('cls')    
                            elif op == 3:
                                print(' Fazer uma transferência...')
                                transferencia = input('Montante(€): ') 
                                os.system('cls')
                            elif op == 4:
                                print('Consultano os Dados do Cliente. . . ')
                            elif op == 5:
                                print(' Saindo da conta...')
                                break

                                
                else:
                       print('Nome ou senha. \033[1;31m Incorreta!!\033[0;0m ')
        else:
            print("Opção inválida. Tente novamente.")
            
        
        sair = input('Clique  [\033[92m enter \033[0m] para continuar ou [\033[91m s \033[0m] para sair: ')
        if sair.lower() == 's':
                break




if __name__ == '__main__':
    
    main()
    