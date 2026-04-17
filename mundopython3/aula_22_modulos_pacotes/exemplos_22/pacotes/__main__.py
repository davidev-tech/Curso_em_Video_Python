from utilidades import numeros

num = int(input('Qual o número? '))
fatorial = numeros.calcular_fatorial(num)
dobro = numeros.calcular_dobro(num)
triplo = numeros.calcular_triplo(num)
print(f'O Fatorial de {num} é {fatorial}')
print(f'O Dobro de {num} é {dobro}')
print(f'O Triplo de {num} é {triplo}')
