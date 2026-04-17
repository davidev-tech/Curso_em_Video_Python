import operacoes

num = int(input('Qual o número? '))
fatorial = operacoes.calcular_fatorial(num)
dobro = operacoes.calcular_dobro(num)
triplo = operacoes.calcular_triplo(num)
print(f'O Fatorial de {num} é {fatorial}')
print(f'O Dobro de {num} é {dobro}')
print(f'O Triplo de {num} é {triplo}')
