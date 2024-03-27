
# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).



class Carrinho:
    def __init__(self):
        self._protudos = []
    
    def total(self):
        return sum([p.preco for p in self._protudos])
    

    def listar_produtos(self):
        print()
        for produto in self._protudos:
            print(f'{produto.nome} ---------------- {produto.preco:.2f}€')
        print()

    def inserir_produtos(self, *produtos):
        """ for produto in produtos:
            self._protudos.append(produto) """
        
        # self._protudos.extend(produtos)
        self._protudos += produtos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
while True:
    prod = input('Nome do produto: ')
    prec = input('Preço (€): ')
    p1 = Produto(prod, float(prec))
    carrinho.inserir_produtos(p1)
    carrinho.listar_produtos()

    ad = input('[clique "Enter" para adicionar produto] ou ["p" para pagar]: ')
    if ad == 'p':
        break
    elif ad == ' ':
        continue

print(f'Total de compras: {carrinho.total():.2f}€')
print()
print()




















