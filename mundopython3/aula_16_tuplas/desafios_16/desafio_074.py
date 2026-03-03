"""
Desafio 074: Gerando números aleatórios e identificando valores extremos em uma Tupla.
"""

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f"Os valores gerados foram:") 
for numero in numeros:
    print(f"{numero}", end=", ")

print(f"\nO maior número gerado foi: {max(numeros)}")
print(f"O menor número gerado foi: {min(numeros)}")