import pandas as pd
"""
Cadastro de Clientes:
    -> Criar uma classe para representar um cliente, com atributos como:
       » nome, CPF, endereço, etc.
       » Implementar funções para permitir que novos clientes se cadastrem no sistema, fornecendo suas informações pessoais.
"""

# Criar uma classe para representar um cliente, com atributos como: nome, CPF, endereço, codigo_postal.
class Cliente:

    def __init__(self, nome, NIF, morada, codigo_postal):
        self._nome = nome
        self._NIF:str = str(NIF)
        self._morada = morada
        self._codigo_postal = codigo_postal
        self._informacao_do_cliente = dict()
    
    def nome(self):  # retorna um nome
        return self._nome
    
    def nif(self): # retorna um NIF
        return self._NIF
    
    def morada(self): # retorna um Morada
        return self._morada
    
    def codigo_postal(self): # retorna um código-postal
        return self._codigo_postal
    

    # Guardar as informções do cliente num dicionário
    def coletar_dados_do_cliente(self):
        self._informacao_do_cliente['Nome'] = self.nome()
        self._informacao_do_cliente['NIF'] = self.nif()
        self._informacao_do_cliente['Morada'] = self.morada()
        self._informacao_do_cliente['Codigo-Postal'] = self.codigo_postal()

        return self._informacao_do_cliente  # Retornar as informações num dicionário
    
    
# Implementar classe e funções para permitir que novos clientes se cadastrem no sistema, fornecendo suas informações pessoais   
class CadastrarCliente(Cliente):

    def __init__(self, nome, NIF, morada, codigo_postal):
        super().__init__(nome, NIF, morada, codigo_postal)
        #self._cliente = {}
        self.arquivo = "C:\\Users\\freds\\Desktop\\curso_de_programacao\\aprender_python\\Projetos_com_python\\Banking_System\\Banco_de_Dados.xlsx"

    def banco_de_dados(self):
        # carregar uma arquivo Excel existente ou criar um DataFrame vazio
        try:
            df = pd.read_excel(self.arquivo) # Tenta carregar uma arquivo Excel existente
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Nome', 'NIF', 'Morada', 'Codigo-Postal'])


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


        

















































