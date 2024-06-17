from cadastro_de_cliente import Cliente
import os
from Validar_nif import validar_nif
import openpyxl
from openpyxl import workbook


class ColetarDados:

    def dados_do_cliente(self):
        print('Insira os seus dados:')
        
        """
        Collects data for a new client and creates a new instance of the Cliente class.
        
        This static method prompts the user to enter various personal identification and contact details for a new client. It then uses this information to create a new instance of the Cliente class. The collected data includes the client's name, age, gender, identification type, identification number, expiration date, marital status, NIF, residence details (country, district, street, postal code), birth details (date, country of birth), contact details (telephone number, email address), and account balance (minimum deposit of 100€).
        
        Returns:
            Cliente: A new instance of the Cliente class with the collected data.
        """
        nome = input('Nome: ')
        idade = input('Idade: ')
        sexo = input('Sexo [M/F]: ').upper()
        
        # validar Nome e NIF aqui mesmo
        while True:
            NIF = input('NIF: ')
            # validar NIF
            if validar_nif(NIF) == True: 
                break
            else:
                print(' NIF inválido! coloque um NIF valido')
                continue
        

        # Carregar o arquivo Excel
        workbook = openpyxl.load_workbook('C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\Banco_de_Dados.xlsx')

        # Selecionar a planilha desejada
        sheet_selecionada = workbook.active

        # Definir a função de comparação
        def cliente_existe(name_cell, nif_cell):
            return name_cell == nome and (nif_cell) == int(NIF)

        # validation of data      
        # Percorrer cada linha na planilha, começando na linha 2 para ignorar o cabeçalho
        nome_encontrado = False
        for row in range(2, sheet_selecionada.max_row + 1): # Go through each line in excel
            name_cell = sheet_selecionada['A%s' % row].value  # percorre a toda linha da coluna "A - Nome"
            nif_cell = sheet_selecionada['H%s' % row].value   # percorre a toda linha da coluna "H - NIF" 

            # If the customer and the NIF exist, he says that the customer is already registered 
            if cliente_existe(name_cell, nif_cell): #  
                nome_encontrado = True
                break
            
        # if not exist, it return False 

        if nome_encontrado:
            return "O cliente já está registado."
        


        identificacao = input('Identificação [PC/T.R]: ')
        n_identificacao = input('Nº de Identificação: ')
        data_de_validade = input('Data de validade: ')
        estado_civil = input('Estado Civil: ')

        print('------------------------------------- ') 


        print('-------------Residência---------------') 
        pais = input('País: ')
        distrito = input('Distrito: ')
        rua = input('Rua: ')
        codigo_postal = input('Código-Postal: ')
        print('------------------------------------- ') 


        print('------------Naturalidade------------- ') 
        data_de_nasc = input('Data de Nascimento (dd/mm/aaaa):  ')
        # validar data de nascimento
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

        # cadastro = CadastrarCliente(nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo)
        
        return novo_cliente