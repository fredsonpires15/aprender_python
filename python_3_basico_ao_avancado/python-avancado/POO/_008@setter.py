
""" Vamos criar uma classe 'ContaBancaria' que representa 
uma conta bancária e que possui um atributo para o saldo 
da conta. Vamos usar um setter para garantir que o saldo 
nunca seja negativo. """


class ContaBancaria:

    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial


    @property
    def saldo(self):
        return
    
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print('ERRO: o saldo não pode ser negativo')
        
        else:
            self._saldo = novo_saldo
            






# Testando a classe
conta = ContaBancaria(100)
if conta.saldo is not None:
    print("Saldo inicial:", conta.saldo)

# Tentando definir um saldo negativo (o setter deve impedir isso)
novo_saldo = conta.saldo = -500

if novo_saldo is not None:
    print("Saldo atual:", novo_saldo)  # Esta linha não será executada devido ao erro

# Verificando se o saldo foi atualizado corretamente
novo_saldo = conta.saldo = 1500
if novo_saldo is not None:
    print("Saldo atualizado:", novo_saldo)




