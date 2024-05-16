import hashlib
import secrets

# Atenção: tem Error neste código, tem que corrigir

class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.salt = secrets.token_hex(16)  # Gerando um salt aleatório
        self._hash_senha = self.hash_senha(senha)

    
    def hash_senha(self, senha):
        # Concatenando a senha com o salt
        senha_salt = senha + self.salt
        print('Senha_selt: ',senha_salt) 
        # Gerando o hash usando SHA-256
        hash_obj = hashlib.sha256(senha_salt.encode())
        """ print('hash_obj: ',hash_obj) """
        return hash_obj.hexdigest()
    
    def nome_usuario(self,usuario):
        return 

    def verificar_senha(self, senha):
        #print(f'{self.hash_senha(senha)}=={self._hash_senha}')
        # Verificando se a senha fornecida corresponde ao hash armazenado
        return self.hash_senha(senha) == self._hash_senha

# Exemplo de uso 
username = "fulano"
senha = "133"

usuario = Usuario(username, senha)

# Verificando a senha
senha_correta = usuario.verificar_senha('133')
#senha_errada = usuario.verificar_senha('234')
print()
#print(f'Salt: {usuario.salt} - tem {len(usuario.salt)} caracteres') 
print()
if senha_correta:
    print("Senha correta:", senha_correta)  # Deve imprimir True
else:
    print('->» Senha Invalida!')
#print("Senha errada:", senha_errada)    # Deve imprimir False
print()
print()






