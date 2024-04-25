
"""
Cadastro de Clientes:
    -> Criar uma classe para representar um cliente, com atributos como:
       » nome, CPF, endereço, etc.
       » Implementar funções para permitir que novos clientes se cadastrem no sistema, fornecendo suas informações pessoais.
"""

# Criar uma classe para representar um cliente, com atributos como: nome, CPF, endereço, etc.



class Cliente:

    def __init__(self, nome,sobrenome, NIF, morada, codigo_postal):
        self._nome = nome
        self._sobrenome = sobrenome
        self._NIF= NIF
        self._morada = morada
        self._codigo_postal = codigo_postal
        self._informacao_do_cliente = dict()

    
    def nome(self):  # retorna um nome
        return self._nome
    
    def sobrenome(self):  # retorna um sobrenome
        return self._sobrenome
    
    def nif(self): # retorna um NIF
        return self._NIF
    
    def morada(self): # retorna um Morada
        return self._morada
    
    def codigo_postal(self): # retorna um código-postal
        return self._codigo_postal
    

    def cliente(self):
        self._informacao_do_cliente['Nome'] = self.nome()
        self._informacao_do_cliente['Sobrenome'] = self.sobrenome()
        self._informacao_do_cliente['NIF'] = self.nif()
        self._informacao_do_cliente['Morada'] = self.morada()
        self._informacao_do_cliente['Codigo-Postal'] = self.codigo_postal()

        # self.informacao_cliente.append(self.nome())
        # self.informacao_cliente.append(self.nif())
        # self.informacao_cliente.append(self.morada())
        # self.informacao_cliente.append(self.codigo_postal())

        return self._informacao_do_cliente 
    
    
# Implementar classe e funções para permitir que novos clientes se cadastrem no sistema, fornecendo suas informações pessoais
    
class CadastrarCliente(Cliente):


    def __init__(self):
        self._cliente = {}
       
    # verificar se o cliente existe
    def verificar_cliente_exitente(self, nif): 

        return nif in self._cliente  # retorna um bool (True or False)
    
    
    # registrar um cliente
    def registrar_cliente(self, cliente):
         
        
        nif = cliente.nif()  # pegar o NIF do cliente


        if not self.verificar_cliente_exitente(nif): # 
            self._cliente[nif] = cliente.cliente()
            print("Cliente registrado com sucesso!")
        else:
            print("Cliente já existe")


        


    

    

    
    

    










    




    




        

if __name__ == '__main__':
    ...















































