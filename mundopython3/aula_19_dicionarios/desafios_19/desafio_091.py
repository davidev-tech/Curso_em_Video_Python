"""
Desafio 091: Ranking de Apostadores com Dicionários.
Implementação de sorteio randômico e ordenação de estruturas não ordenadas
utilizando sorted() e operator.itemgetter para critérios de valor.
"""
from random import randint
from time import sleep
from operator import itemgetter

jogos = {"jogador1": randint(1,6),
        "jogador2": randint(1,6),
        "jogador3": randint(1,6),
        "jogador4": randint(1,6)
       }

ranking = sorted(jogos.items(), key=itemgetter(1), reverse= True)
print("Ranking dos jogadores: ")
for i, v in enumerate(ranking):
    print(f"{i + 1}° lugar: {v[0]} com {v[1]} Pontos.")
    sleep(1)