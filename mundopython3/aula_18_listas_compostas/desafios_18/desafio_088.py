"""
Desafio 088: Simulador de palpites para a Mega Sena.
Implementação de sorteio estatístico com prevenção de duplicatas (Membership Testing)
e armazenamento em estruturas de listas compostas com controle de fatiamento [[:]].
"""
from random import randint
from time import sleep

print("-" * 30)
print(f"{"JOGO NA MEGA SENA":^30}")
print("-" * 30)

palpites_mega_sena = []
quantidade_palpites = int(input("Quantos jogos deseja que eu sorteie? "))
valores_palpites = []
palpites = 0

while palpites < quantidade_palpites:
    while len(valores_palpites) < 6:
        sorteio = randint(0, 60)
        numero_palpite = sorteio
        if numero_palpite not in valores_palpites:
            valores_palpites.append(numero_palpite)
    palpites_mega_sena.append(valores_palpites[:])
    valores_palpites.clear()
    palpites += 1

for palpite in palpites_mega_sena:
    palpite.sort()
    print(f"O palpite gerado foi: {palpite}")
    sleep(2)