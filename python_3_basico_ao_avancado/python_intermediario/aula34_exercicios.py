# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    mult = 1
    for numero in args:
        mult *= numero
    return mult

def par_impar(num):
    if num % 2 == 0:
        return 'Numero Par'
     
    return ' Numero Impar'
    
valor = multiplicar(2,3,4,5,6)


print(valor) 
print(par_impar(32))
print(par_impar(2))
print(par_impar(5))