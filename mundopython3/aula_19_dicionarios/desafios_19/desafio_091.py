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

print(f"Valores sorteados:")
for k, v in jogos.items():
    sleep(1)
    print(f"{k} tirou {v} no dado.")

ranking = sorted(jogos.items(), key=itemgetter(1), reverse= True)   
print("-=" * 40)
print(" == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    sleep(1)
    print(f"{i + 1}° lugar: {v[0]} com {v[1]} Pontos.")
    