

# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []


    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        return self.enderecos

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Paulo')
cliente1.inserir_endereco('Rua Cidade de praia', 5)
cliente1.inserir_endereco('Av. Heróris de Ultramar', 35)
cliente1.listar_endereco()


















































