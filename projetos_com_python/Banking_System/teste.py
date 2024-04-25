from cadastro_de_cliente import Cliente, CadastrarCliente
from colorama import Fore, Back, Style

print()


if __name__ == '__main__':
    
    listar_clientes = []  # Lista para armazenar os clientes registrados

    while True:
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
""" while True:
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        NIF = input('NIF: ') 
        morada = input('Morada: ') 
        codigo_postal = input('Código Postal: ')

        cadastro = CadastrarCliente()

        # Criando um novo cliente
        novo_cliente = Cliente(nome, sobrenome, NIF, morada, codigo_postal)

        # Verificando se o cliente já existe e registrando-o se não existe
        cadastro.registrar_cliente(novo_cliente)

        # Adicionando o cliente à lista de clientes
        listar_clientes.append(novo_cliente.cliente())

        sair = input('Clique  [\033[92m enter\033[0m] para continuar ou [\033[91m s\033[0m] para sair: ')
        if sair.lower() == 's':
            break

    # Após sair do loop, exibir a lista de clientes registrados
    print("Clientes registrados:")
    for cliente in listar_clientes:
        print(cliente) """
        

    

        



