import pandas as pd

# Defina o caminho para o arquivo Excel
arquivo_excel = 'clientes.xlsx'

# Tente carregar o arquivo Excel existente ou crie um DataFrame vazio
try:
    df = pd.read_excel(arquivo_excel)
except FileNotFoundError:
    df = pd.DataFrame(columns=['nome', 'endereco', 'telefone', 'email'])

# Crie uma função para coletar dados de um cliente
def coletar_dados_cliente():
    print("Informe os dados do cliente")
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    return {'nome': nome, 'endereco': endereco, 'telefone': telefone, 'email': email}

# Loop para cadastrar clientes indefinidamente
while True:
    # Coletar os dados do cliente
    cliente = coletar_dados_cliente()
    
    # Crie um DataFrame com os dados do cliente
    cliente_df = pd.DataFrame([cliente])
    
    # Concatene o novo cliente ao DataFrame existente
    df = pd.concat([df, cliente_df], ignore_index=True)
    
    # Perguntar ao usuário se deseja continuar cadastrando
    continuar = input("Deseja cadastrar outro cliente? (s/n): ").lower()
    if continuar != 's':
        break

# Salve os dados de volta no arquivo Excel
df.to_excel(arquivo_excel, index=False)

print("Os dados dos clientes foram salvos com sucesso no arquivo Excel.")