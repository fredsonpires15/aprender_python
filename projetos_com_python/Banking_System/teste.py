from cadastro_de_cliente import Cliente, CadastrarCliente
from colorama import Fore, Back, Style
from validar import validar_usuario
from estrutura import menu_login, menu
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

        if op == 1:
                print('------------Sua Identificação--------------')
                nome = input('Nome: ')
                idade = input('Idade: ')
                sexo = input('Sexo [M/F]: ').upper()
                identificacao = input('Identificação [PC/T.R]: ')
                n_identificacao = input('Nº de Identificação: ')
                data_de_validade = input('Data de validade: ')
                estado_civil = input('Estado Civil: ')
                NIF = input('NIF: ')
                print('------------------------------------- ') 


                print('-------------Residência---------------') 
                pais = input('País: ')
                distrito = input('Distrito: ')
                rua = input('Rua: ')
                codigo_postal = input('Código-Postal: ')
                print('------------------------------------- ') 


                print('------------Naturalidade------------- ') 
                data_de_nasc = input('Data de Nascimento:    ')
                pais_de_nasc = input('País: ')
                print('------------------------------------- ') 


                print('--------------Contacto--------------- ') 
                telemovel = input('Telemóvel: ')
                e_mail = input('E-mail: ')
                print('------------------------------------- ') 
                
                os.system('cls')
                print('------------Abrir Conta-------------- ')
                
                print('Para concluir o processo, faça um depósito de no minimo 100€. \n Nota: Depois da abertura da conta o cliente pode poderá sacar o seu dinheiro quando quiser!!  ')
                saldo = float(input('Montante(€): '))
                


                # Criando um novo cliente
                novo_cliente = Cliente(nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo)

                cadastro = CadastrarCliente(nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo)

                cadastro.banco_de_dados()

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
                                os.system('cls')
                                if op == 1:
                                        print(' Mostrar Dados do usuário...')
                                        print('---identificação---------------------')
                                        print('|                                   |')
                                        print('|                 Nome:             |')
                                        print('|                 Sexo:             |')
                                        print('|Identificação [PC/TR]:             |')
                                        print('|      Nºidentificação:             |')
                                        print('|     Data de validade:             |')
                                        print('|                  NIF:             |')
                                        print('|         Estado Civil:             |')
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

for cliente in listar_clientes:
        print(cliente)   

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



        



