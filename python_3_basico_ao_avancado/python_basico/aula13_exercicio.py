nome = (input('Digite seu nome:'))
idade = (input('Sua idade:'))
if nome  and  idade:
    print(f'seu nome é {nome}')
    print(f'Seu nome ivertido é {nome[::-1]} ')
    print(f'Meu nome contém espaços? {" " in nome}')
    print(f'Seu nome tem {len(nome)}')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    print('')
else:
    print('Desculpe, você deixou campos vazios.')
   