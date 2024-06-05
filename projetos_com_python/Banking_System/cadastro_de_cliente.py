import pandas as pd
import gerar_IBAN
import random
from Validar_nif import validar_nif
import os
import openpyxl
from openpyxl import workbook
"""
Cadastro de Clientes:
    -> Criar uma classe para representar um cliente, com atributos como:
       » nome, CPF, endereço, etc.
       » Implementar funções para permitir que novos clientes se cadastrem no sistema, fornecendo suas informações pessoais.
"""

# Criar uma classe para representar um cliente, com atributos como: nome, CPF, endereço, codigo_postal.
class Cliente:

    def __init__(self, nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo):
        """
        Initializes a new instance of the Cliente class with the given parameters.
        Parameters:
            nome (str): The name of the client.
            idade (int): The age of the client.
            sexo (str): The gender of the client.
            identificacao (str): The identification document of the client.
            n_identificacao (str): The identification number of the client.
            data_de_validade (str): The expiration date of the identification document.
            estado_civil (str): The marital status of the client.
            NIF (str): The National Identification Number of the client.
            pais (str): The country of the client.
            distrito (str): The district of the client.
            rua (str): The street of the client's address.
            codigo_postal (str): The postal code of the client's address.
            data_de_nasc (str): The date of birth of the client.
            pais_de_nasc (str): The country of birth of the client.
            telemovel (str): The client's phone number.
            e_mail (str): The client's email address.
            saldo (float): The client's balance.

        Returns:
            None
        """
        self._idade = idade
        self._sexo = sexo
        self._identificacao = identificacao
        self._n_identificacao = n_identificacao
        self._data_de_validade = data_de_validade
        self._estado_civil = estado_civil
        self._NIF:str = str(NIF)
        self._pais = pais
        self._distrito = distrito
        self._rua = rua
        self._codigo_postal = codigo_postal
        self._data_de_nasc = data_de_nasc
        self._pais_de_nasc = pais_de_nasc
        self._telemovel = telemovel
        self._email = e_mail
        self._saldo = saldo
        self._informacao_do_cliente = dict() 
        self._arquivo = "C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\Banco_de_Dados.xlsx"

        
    def nome(self):  # retorna um nome
        return self._nome
    
    def idade(self):
        return self._idade
    
    def sexo(self):
        return self._sexo
    
    def identificacao(self):
        return self._identificacao
    
    def n_identificacao(self):
        return self._n_identificacao
    
    def data_de_validade(self):
        return self._data_de_validade
    
    def estado_civil(self):
        return self._estado_civil

    def nif(self): # retorna um NIF
        return self._NIF
     
    # ---Dados da Residência------------------------
    def pais(self):
        return self._pais
    
    def distrito(self):
        return self._distrito
    
    def rua(self):
        return self._rua
        
    def codigo_postal(self): # retorna um código-postal
        return self._codigo_postal
    
    # ---Naturalidade----------------------

    def data_de_nasc(self): 
        return self._data_de_nasc
    
    def pais_de_nasc(self): 
        return self._pais_de_nasc
    
    #---Contacto--------------------------

    def telemovel(self):
        return self._telemovel
    
    def email(self):
        return self._email
    
    # -----Dados da Conta----------

    def saldo(self):
        """
        Returns the current balance of the account.

        :return: The balance of the account as a float.
        """
    
    @staticmethod
    def coletar_dados_Client():
        """
        Collects data for a new client and creates a new instance of the Cliente class.
        
        This static method prompts the user to enter various personal identification and contact details for a new client. It then uses this information to create a new instance of the Cliente class. The collected data includes the client's name, age, gender, identification type, identification number, expiration date, marital status, NIF, residence details (country, district, street, postal code), birth details (date, country of birth), contact details (telephone number, email address), and account balance (minimum deposit of 100€).
        
        Returns:
            Cliente: A new instance of the Cliente class with the collected data.
        """
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

        # cadastro = CadastrarCliente(nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo)
        
        return novo_cliente 
        
      

    # Criar um função chamada **guardar_dados_do_cliente(*self*) que retorna dados do cliente Guardar as informções do cliente num dicionário
    def guardar_dados_do_cliente(self):
        """
        Returns a dictionary containing the personal data of a client.

        :return: A dictionary with the following keys:
                    - 'Nome' (str): The client's name.
                    - 'Idade' (int): The client's age.
                    - 'Sexo' (str): The client's gender.
                    - 'Identificação' (str): The client's identification type.
                    - 'N_Identificação' (str): The client's identification number.
                    - 'Data_de_Validade' (date): The client's identification expiration date.
                    - 'Estado_Civil' (str): The client's marital status.
                    - 'NIF' (str): The client's tax identification number.
                    - 'País' (str): The client's country of residence.
                    - 'Distrito' (str): The client's district.
                    - 'Rua' (str): The client's street address.
                    - 'Codigo_Postal' (str): The client's postal code.
                    - 'Data_de_Nasc' (date): The client's date of birth.
                    - 'País_de_Nasc' (str): The client's country of birth.
                    - 'Telemóvel' (str): The client's mobile phone number.
                    - 'Email' (str): The client's email address.
                    - 'Saldo' (float): The client's account balance.
        """
        return dict(
            Nome=self.nome(),
            Idade=self.idade(),
            Sexo=self.sexo(),
            Identificação=self.identificacao(),
            N_Identificação=self.n_identificacao(),
            Data_de_Validade=self.data_de_validade(),
            Estado_Civil=self.estado_civil(),
            NIF=self.nif(),
            País=self.pais(),
            Distrito=self.distrito(),
            Rua=self.rua(),
            Codigo_Postal=self.codigo_postal(),
            Data_de_Nasc=self.data_de_nasc(),
            País_de_Nasc=self.pais_de_nasc(),
            Telemóvel=self.telemovel(),
            Email=self.email(),
            Saldo=self.saldo()

        )  # Retornar as informações num dicionário
    

    # Criar uma função **banco_de_dados(*self*) que guarda todas as dados do cliente num banco de dados**
    def banco_de_dados(self):
        """
        Saves the data of a client to an Excel file.

        This function loads an existing Excel file or creates an empty DataFrame if the file does not exist.
        It then collects the data of the client by calling the `guardar_dados_do_cliente` method.
        The data is stored in a DataFrame called `cliente_df`.
        The function concatenates the new client's data with the existing DataFrame using the `pd.concat` method.
        Finally, the function saves the updated DataFrame to the Excel file specified by the `_arquivo` attribute.

        Parameters:
        - self: The instance of the class.

        Returns:
        - None

        Prints:
        - "[\033[92m Os dados dos clientes foram salvos com sucesso no _arquivo Excel.\033[0m]" if the data is successfully saved.
        """
        try:
            df = pd.read_excel(self._arquivo)  # Tenta carregar uma arquivo Excel existente
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nome', 'Idade', 'Sexo', 'Identificação','N_Identificação','Data_de_Validade', 'Estado_Civil', 'NIF', 'País', 'Distrito', 'Rua','Codigo_Postal', 'Data_de_Nasc', 'País_de_Nasc', 'Telemóvel', 'Email', 'Saldo' ])

    
        # coletar os dados do cliente 
        cliente = self.guardar_dados_do_cliente()

        #criar um DataFrame com os dados do cliente
        cliente_df = pd.DataFrame([cliente])

        #concatenar o novo cliente ao DataFrame existente
        df = pd.concat([df, cliente_df], ignore_index=True)

        # Envair os dados para um ficheiro excel
        df.to_excel(self._arquivo, index=False)
        
        print(" [\033[92m Os dados dos clientes foram salvos com sucesso no _arquivo Excel.\033[0m]")
    
    # Create a function called 'validar_cliente' that enters the database and checks if the client exists.
    def validar_cliente(self):

        """
        
        """
        sheet_selecionada = self._arquivo['Sheet1']

        # validation of data      
        if self.validaar_nif(): 
            for row in range(2, len(sheet_selecionada['A']) + 1): # Go through each line in excel
                name_cell = sheet_selecionada['A%s' % row].value  # percorre a toda linha da coluna "A - Nome"
                nif_cell = sheet_selecionada['H%s' % row].value   # percorre a toda linha da coluna "H - NIF" 

                # If the customer and the NIF exist, he says that the customer is already registered 
                if name_cell == self.nome() and nif_cell == self.nif(): #  
                       raise ValueError('O Cliente já está cadastrado.')
                
                # if not exist, it return False  
                else: 
                    return False        
        else:
            raise ValueError('NIF inválido!!')
        
        
    
    #Validar automaticamente o NIF ao registrar um novo cliente
    def validaar_nif(self):
        """
        Validates the NIF (Portuguese citizen number) of the current instance.

        This function calls the `validar_nif` function from the `Validar_nif.py` module with the current instance's NIF as an argument. It then returns the result of the `validar_nif` function.

        Returns:
            bool: True if the NIF is valid, False otherwise.
        """
        val = validar_nif(self.nif())
        return val    
    
    # create new accounts
    def create_account(self, client, type_account, initial_balance):
        """
        Creates a new bank account for a given client with the specified account type and initial balance.

        Args:
            client (Cliente): The client for whom the account is being created.
            type_account (str): The type of account (e.g., "Poupança", "Corrente").
            initial_balance (float): The initial balance of the account.

        Raises:
            ValueError: If the initial balance is negative.

        Returns:
            None
        """
        
        sheet_selecionada = self._arquivo['Sheet1']

        # validation of data
        for row in range(2, len(sheet_selecionada['A']) + 1):
            if sheet_selecionada['A%s' % row].value  == self.nome():
                if sheet_selecionada['Q%s' % row].value < 0:
                    raise ValueError('O saldo inicial não pode ser negativo. ')
        
        # Geneation of  the account number
        
        account_number  = gerar_IBAN.iban()

    
class BankAccount:
    def __init__(self, client, num_account,type_account, initial_balance):
        """
        Initializes a new instance of the BankAccount class.

        Parameters:
            client (Cliente): The client associated with the bank account.
            num_account (int): The account number.
            type_account (str): The type of account (e.g., "Poupança", "Corrente").
            initial_balance (float): The initial balance of the account.

        Returns:
            None
        """
        self.type_account = type_account
        self.initial_balance = initial_balance
        self.client = client

      


        """ codigo_pais = "ST"  # Código do país para a Portugal
        banco = "50010517"  # Código do banco
        agencia = "000"
        conta = "123456789"

        iban = gerar_IBAN.gerar_iban(codigo_pais, banco, agencia, conta)
                
        if Cliente.validar_cliente():
            ...
        """
        # Definir o tipo de conta**: Escolher o tipo de conta desejada (e.g., Poupança, Corrente).


        # Definir o saldo inicial**: Definir o valor inicial a ser depositado.

        # Vincular a conta ao cliente**: Associar a conta ao cliente e adicionar a conta à lista de contas do cliente.

        pass

    def iban(self):
        """
        Returns the IBAN (International Bank Account Number) generated by the `gerar_IBAN` module.

        :return: The generated IBAN.
        :rtype: str
        """
        return gerar_IBAN.iban() 

    # função que mostra dados do usuario ou cliente
    def consultar_informacoes(self):
        """
        Retrieves and displays information about a specific user.

        This function loads the 'Banco_de_Dados.xlsx' workbook and searches for the user with the name in the 'Sheet1' sheet. If the user is found, their identification, residence, naturalization, and contact information are printed to the console.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        book = openpyxl.load_workbook(filename= 'Projetos_com_python/Banking_System/Banco_de_Dados.xlsx')
        nome = 'Fredson Vila Nova'
        ws = workbook
        sheet_selecionada = book['Sheet1']
        for row in range(2, len(sheet_selecionada['A'])+1):
            if sheet_selecionada['A%s' % row].value == nome:
                print(' Mostrar Dados do usuário...')
                print( '---identificação---------------------------------')
                print(f'|{" "*1:<47}|')
                print(f'|                 Nome: {sheet_selecionada["A%s" % row].value:<24}|')
                print(f'|                Idade: {sheet_selecionada["B%s" % row].value:<24}|')
                print(f'|                 Sexo: {sheet_selecionada["C%s" % row].value:<24}|')
                print(f'|Identificação [PC/TR]: {sheet_selecionada["D%s" % row].value:<24}|')
                print(f'|      Nºidentificação: {sheet_selecionada["E%s" % row].value:<24}|')
                print(f'|     Data de validade: {sheet_selecionada["F%s" % row].value:<24}|')
                print(f'|         Estado Civil: {sheet_selecionada["G%s" % row].value:<24}|')
                print(f'|                  NIF: {sheet_selecionada["H%s" % row].value:<24}|')
                print( '-------------------------------------------------')
                print('')
                print( '---Residência------------------------------------')
                print(f'|{" "*1:<47}|')
                print(f'|                 País: {sheet_selecionada["I%s" % row].value:<24}|')
                print(f'|             Distrito: {sheet_selecionada["J%s" % row].value:<24}|')
                print(f'|                  Rua: {sheet_selecionada["K%s" % row].value:<24}|')
                print(f'|        Código-Postal: {sheet_selecionada["L%s" % row].value:<24}|')
                print( '-------------------------------------------------')
                print('')
                print( '---Naturalidade----------------------------------')
                print(f'|{" "*1:<47}|')
                print(f'|     Data de Nascimento: {sheet_selecionada["M%s" % row].value:<22}|')
                print(f'|                   País: {sheet_selecionada["N%s" % row].value:<22}|')
                print(' -------------------------------------------------')
                print('')
                print('---Contacto--------------------------------------')
                print(f'|{" "*1:<47}|')
                print(f'|              Telemóvel: {sheet_selecionada["O%s" % row].value:<22}|')
                print(f'|                 E-mail: {sheet_selecionada["P%s" % row].value:<22}|')
                print('--------------------------------------------------')
                
                depositar = input('Montante(€): ')
                os.system('cls')



  #----------- Authentication and security -------- -
class Authentication:
    
    def __init__(self):
        """
        Initializes an instance of the class.
        """
        pass

    def register(self, usuario, senha):
        """
        Registers a new user with the given username and password.

        Parameters:
            usuario (str): The username of the user.
            senha (str): The password of the user.

        Returns:
            None
        """
        pass

    def login(self, usuario, senha):
        """
        Logs in a user with the given username and password.

        Parameters:
            usuario (str): The username of the user.
            senha (str): The password of the user.

        Returns:
            None
        """
        pass

class Transactions:

    #Realizar depósitos
    def deposit(self, conta, value):
        'logic to deposit'
        pass

    #Realizar saques
    def withdraw(self, conta, value):
        'Logic to withdraw mony'
        pass

    #Realizar transferências entre contas
    def transfer(self, account_origin, account_destiny, value ):
        'logic to transfers'

        #Verificar se há saldo suficiente para as transações
        pass


    # -------Gestão de Saldo---------

    class GestaoSaldo:

        # Atualizar saldo da conta após transação
        def atualizar_saldo(self, conta):
            "Logic to atualizar saldo"
            conta

        def consultar_saldo(self, conta):
            "Logic to atualizar saldo"
            conta
            pass
        



# Implementar classe e funções para permitir que novos clientes se cadastrem no sistema, fornecendo suas informações pessoais   
class CadastrarCliente(Cliente):

    def __init__(self,nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo):
        super().__init__(nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail,saldo)
        #self._cliente = {}

    """ # verificar se o cliente existe
    def verificar_cliente_exitente(self, nif):
      
        return nif in self._cliente  # retorna um bool (True or False)
      
    # registrar um novo cliente
    def registrar_cliente(self, cliente):
             
        nif = cliente.nif()  # pegar o NIF do cliente
        
        if not self.verificar_cliente_exitente(nif): # se o NIF não existir 
            self._cliente[nif] = cliente.guardar_informacao() # adiciona o NIF
            print("Cliente registrado com sucesso!")
        else:
            print("Cliente já existe") """















































