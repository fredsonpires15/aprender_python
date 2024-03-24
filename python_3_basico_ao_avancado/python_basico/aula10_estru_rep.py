# if / elif       / else
# se / se não se / se ñão

primeiro = input('Digite um valor:')
segundo = input('Digite outro valor:')
if primeiro > segundo:
    print(f'O número {primeiro} é maior que {segundo}')
elif primeiro < segundo:
    print(f'O número {segundo} é maior qe {primeiro}')
else:
    print('Ambos são iguais')

