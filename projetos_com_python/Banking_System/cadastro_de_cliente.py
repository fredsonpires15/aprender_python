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
        self._nome = nome
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
        return self._saldo 
    
    @staticmethod
    def coletar_dados_Client():
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

        # cadastro = CadastrarCliente(nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo)
        
        return novo_cliente 
        
      

    # Criar um função chamada **guardar_dados_do_cliente(*self*) que retorna dados do cliente Guardar as informções do cliente num dicionário
    def guardar_dados_do_cliente(self):
        
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
        # carregar uma arquivo Excel existente ou criar um DataFrame vazio 
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
        val = validar_nif(self.nif())
        return val    
    
    # create new accounts
    def create_account(self, client, type_account, initial_balance):
        # Generate a unique account number**: Can be generated automatically
        
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
        self.num_account = num_account
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
        return gerar_IBAN.iban() 

    # função que mostra dados do usuario ou cliente
    def consultar_informacoes(self):

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
        pass

    def register(self, usuario, senha):
        pass

    def login(self, usuario, senha):
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
            pass

        def consultar_saldo(self, conta):
            "Logic to atualizar saldo"
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















































