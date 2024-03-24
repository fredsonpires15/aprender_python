def criar_saudacoes(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacoes('Bom Dia')
falar_bom_noite = criar_saudacoes('Boa Noite')
for nome in ['Pedro', 'nanda','Edy']:
    print(falar_bom_dia(nome))
    print(falar_bom_noite(nome))
