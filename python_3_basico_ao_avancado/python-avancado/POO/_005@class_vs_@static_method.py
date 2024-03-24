""" method vs @classmethod vs @staticmethod
method - self, método de instância
@classmethod - cls, método da classe
@staticmethod - método estatico (não - self, não - cls) """

class connection:


    def __init__(self, host='localhost') :
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user


    def set_password(self, password):
        self.password = password


    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def msg(msg):
        return f'SMS: {msg}' 
        




#c1 = connection()
c1 = connection.create_with_auth('Nome do Usuario:', 'Palavra-passe: ' )

# c1.set_user('Nome do Usuario:  ')
# c1.set_password('Palavra-passe: ')

print(connection.msg('Este é um método estático!!'))
print(c1.user)
print(c1.password)

