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


t = {'Nome': 'Fredson ', 'Sobrenome': 'Vila Nova', 'NIF': '308806662', 'Morada': 'AV. rua 123', 'Codigo-Postal': '7005-161'}

print('308806662' in t['NIF'])

