

def validar_senha_usuario(nome, senha, nomes_validos, senhas_validas):


    #verificar ese nome está em nomes válidos
    if nome not in nomes_validos:
        print(" \033[1;31m Nome Inválido!!\033[0;0m")
        return False 
    #verificar se a senha está em senhas válidas
    if senha not in senhas_validas:
        print("\033[1;31m Senha Inválida!!\033[0;0m")
        return False
    
    return True 












