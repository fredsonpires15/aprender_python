import pandas as pd
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


    # Guardar as informções do cliente num dicionário
    def coletar_dados_do_cliente(self):
        # self._informacao_do_cliente['Nome'] = self.nome()
        # self._informacao_do_cliente['NIF'] = self.nif()
        # self._informacao_do_cliente['Morada'] = self.morada()
        # self._informacao_do_cliente['Codigo-Postal'] = self.codigo_postal() 
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
    
    
# Implementar classe e funções para permitir que novos clientes se cadastrem no sistema, fornecendo suas informações pessoais   
class CadastrarCliente(Cliente):

    def __init__(self,nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail, saldo):
        super().__init__(nome,idade,sexo,identificacao,n_identificacao,data_de_validade,estado_civil, NIF,pais,distrito,rua, codigo_postal, data_de_nasc,pais_de_nasc,telemovel,e_mail,saldo)
        #self._cliente = {}
        self.arquivo = "C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\Banco_de_Dados.xlsx"

    def banco_de_dados(self):
        # carregar uma arquivo Excel existente ou criar um DataFrame vazio 
        try:
            df = pd.read_excel(self.arquivo)  # Tenta carregar uma arquivo Excel existente
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nome', 'Idade', 'Sexo', 'Identificação','N_Identificação','Data_de_Validade', 'Estado_Civil', 'NIF', 'País', 'Distrito', 'Rua','Codigo_Postal', 'Data_de_Nasc', 'País_de_Nasc', 'Telemóvel', 'Email', 'Saldo' ])


        # coletar os dados do cliente 
        cliente = self.coletar_dados_do_cliente()

        #criar um DataFrame com os dados do cliente
        cliente_df = pd.DataFrame([cliente])

        #concatenar o novo cliente ao DataFrame existente
        df = pd.concat([df, cliente_df], ignore_index=True)

        #Envair os dados para um 
        df.to_excel(self.arquivo, index=False)
        
        print(" [\033[92m Os dados dos clientes foram salvos com sucesso no arquivo Excel.\033[0m]")
    
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


        

















































