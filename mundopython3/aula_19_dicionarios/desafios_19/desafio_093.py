"""
Desafio 093: Cadastro de Jogador de Futebol.
Gerenciamento de estatísticas esportivas utilizando composição de estruturas:
Dicionário (Perfil do Atleta) contendo Lista (Histórico de Gols).
Uso de sum() para totalização automatizada de performance.
"""
ficha_jogador = {}
gols_partida = []
total_gols = 0

ficha_jogador['nome'] = str(input("Qual o nome do Jogador: "))
ficha_jogador['partidas_jogadas'] = int(input(f"Quantas partidas {ficha_jogador['nome']} jogou? "))

for partida in range(ficha_jogador['partidas_jogadas']):
    gols = int(input(f"Quantos gols na {partida + 1}° Partida? "))
    gols_partida.append(gols)

ficha_jogador['gols_partida'] = gols_partida[:]
ficha_jogador['total_gols'] = sum(gols_partida)

print("-=" * 18)
print(f"O jogador {ficha_jogador['nome']} jogou {ficha_jogador['partidas_jogadas']} Partidas.")
for i, v in enumerate(ficha_jogador['gols_partida']):
    print(f"    => Na {i + 1}° Partida fez {v} gols.")
print("-=" * 18)
print(f"{ficha_jogador['nome']} teve um total de {ficha_jogador['total_gols']} em {ficha_jogador['partidas_jogadas']} Partidas.")