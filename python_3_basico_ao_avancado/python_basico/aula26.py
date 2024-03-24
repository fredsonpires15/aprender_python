import os

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
lista = []
while True:
    print('[1] -> Inserir \n[2] -> Apagar \n[3] -> Listar')
    opcao = input('Sua Opção:') or ''
    
    if opcao == '1':
        os.system('cls')
        inserir = input('O que deseja inserir:')
        lista.append(inserir)


    elif opcao == '2':
       
       apagar = (input('Escolha um índice para apagar:'))
       try:
           indice = int(apagar)
           del lista[indice]
       except ValueError:
           print('Por favor, digite um número inteiro.')
       except IndexError:
           print('Este indice não existe na lista.')
       except Exception:
           print('Erro desconhecido....!!!!!')
        
       
    elif opcao == '3':
        os.system('cls')

        if len(lista) == 0:
            print('Nada na lista')
        else:
            for i, elemento in enumerate(lista):
                print(i, elemento)
    elif opcao == '':
        print('Você esqueceu de indicar a sua opção. Tente novamente!!')
    else:
        print('Opção inválida. Tente novamente!!')
        continue