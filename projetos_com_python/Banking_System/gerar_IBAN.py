def gerar_iban(codigo_pais, banco, agencia, conta):
    # Combine os elementos necessários para o IBAN
    elementos = f"{banco}{agencia}{conta}"
    
    # Adicione o código do país e os dígitos de verificação
    iban_inicial = f"{codigo_pais}00{elementos}"
    
    # Calcule os dígitos de verificação usando a função de cálculo específica
    verificador = calcular_digitos_verificacao(iban_inicial)
    
    # Substitua os dígitos de verificação no IBAN
    iban = f"{codigo_pais}{verificador}{elementos}"
    
    return iban

def calcular_digitos_verificacao(iban):
    # Converter IBAN para uma string numérica para cálculo
    iban_numerico = converter_para_numerico(iban)
    
    # Calcule os dígitos de verificação usando mod 97
    verificador = 98 - (int(iban_numerico) % 97)
    
    # Retorne os dígitos de verificação formatados com dois dígitos
    return f"{verificador:02d}"

def converter_para_numerico(iban):
    # Converta cada caractere do IBAN para números
    iban_numerico = ''
    for char in iban:
        if char.isalpha():
            iban_numerico += str(ord(char.upper()) - ord('A') + 10)
        else:
            iban_numerico += char
    
    return iban_numerico

# Exemplo de uso:
# codigo_pais = "ST"  # Código do país para a Portugal
# banco = "50010517"  # Código do banco
# agencia = "000"
# conta = "123456789"

# iban = gerar_iban(codigo_pais, banco, agencia, conta)
# print("IBAN gerado:", iban)



