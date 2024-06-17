
import xlsxwriter as xw 
import os

from cadastro_de_cliente import Cliente, CadastrarCliente
from colorama import Fore, Back, Style
from validar import validar_usuario
from estrutura import menu_login, menu, dados_cliente
from Coletar_Dados import ColetarDados
import os



print()
if __name__ == '__main__':
    
    nome_valido = 'Fredson'
    senha_valida = '123'
    
    listar_clientes = []  # Lista para armazenar os clientes registrados

    while True:
        menu_login() # fazer login ou cadastro
        op = int(input('Opção: ') )
        os.system('cls')
        #print(Cliente.coletar_dados_Client().validar_cliente())

        if op == 1:
            novo_cliente = ColetarDados()
            
            cliente = novo_cliente.dados_do_cliente()

            validar = cliente.validar_cliente()

            if validar == True:
                print('O Cliente já foi registrado ')
                break

            else:
                print()
                cliente.banco_de_dados()
                break



            # if Cliente.coletar_dados_Client().validar_cliente()== False:
            #     Cliente.coletar_dados_Client().banco_de_dados(Cliente)

            # else:
            #     Cliente.validar_cliente()

            # Verificando se o cliente já existe e registrando-o se não existe
            #cadastro.registrar_cliente(novo_cliente)

            # Adicionando o cliente à lista de clientes
            #listar_clientes.append(novo_cliente.guardar_informacao().copy())

        elif op == 2:
                nome = input('Nome do usúario: ')
                senha = input('Senha: ')
                os.system('cls')

                if  validar_usuario(nome,senha, nome_valido, senha_valida):
                        while True:
        
                            menu()
                            op = int(input('Opção: ') )
                            print()
                            print()
                            os.system('cls')

                            if op == 1:
                                    dados_cliente()
                            elif op == 2:
                                print(' Realizar um deposito...')
                                depositar = input('Montante(€): ')
                                os.system('cls')    
                            elif op == 3:
                                print(' Sacar dinheiro na conta...')
                                sacar = input('Montante(€): ') 
                                os.system('cls')
                            elif op == 4:
                                print(' Fazer uma transferência...')
                            elif op == 5:
                                print(' Saindo da conta...')
                                break

                                
                else:
                       print('Nome ou senha. \033[1;31m Incorreta!!\033[0;0m ')
        
        sair = input('Clique  [\033[92m enter\033[0m] para continuar ou [\033[91m s\033[0m] para sair: ')
        if sair.lower() == 's':
                break

        # # Após sair do loop, exibir a lista de clientes registrados
        # print("Clientes registrados:")
        # for cliente in not  listar_clientes:
        #         if cliente['NIF'] == NIF:
        #                 print(cliente)


print('____________________________________________________________________')
 

print('____________________________________________________________________')
    

"""  while True:
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        NIF = input('NIF: ') 
        morada = input('Morada: ') 
        codigo_postal = input('Código Postal: ')

        cadastro = CadastrarCliente()

        # Criando um novo cliente
        novo_cliente = Cliente(nome, sobrenome, NIF, morada, codigo_postal)
        #cadastro.registrar_cliente(novo_cliente)
     
        cadastro.verificar_cliente_exitente(novo_cliente)
"""



        







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


