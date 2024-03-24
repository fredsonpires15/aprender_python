import random

times = (
'SL Benfica',	 'FC Porto',	
'SC Braga',	     'Sporting CP',	
'Vitória SC	',	 'Casa Pia AC',	
'FC Arouca',	 'Boavista FC',	
'FC Vizela',	 'Gil Vicente',	
'Rio Ave FC',	 'FCFamalicão',	
'Portimonense',   'GD Chaves',	
'EstorilPraia',	 'Marítimo M.',	
'Santa Clara',   'FC P.Ferreira'
)

print(f'Primeiros classificados:{times[0:5]}')
print('-='*20)
print('')

print(f'Os últimos colocados{times[-4:]}')
print('-='*20)
print('')
print(f'por ordem alfabética:{sorted(times)}')
print('')
print('-='*40)
print('     Jogos da segunda mão:')
for _ in range(3):
    print(f'     {random.choice(times)}   x   {random.choice(times)}')
    print(' ')
print('-='*40) 
