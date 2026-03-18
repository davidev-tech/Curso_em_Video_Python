"""
Desafio 095: Sistema Gerenciador de Performance de Atletas.
Consolidação de estruturas compostas: Lista de Dicionários com Listas Internas.
Implementação de Busca Indexada O(1) e Interface de Tabela Formatada.
"""
ficha_jogadores = []
ficha_jogador = {}

while True:
    ficha_jogador.clear()
    gols_partidas = []
    total_gols = 0
    continuar_parar = " "

    ficha_jogador['nome'] = str(input("Qual o nome do jogador? "))
    ficha_jogador['partidas_jogadas'] = int(input(f"Quantas partidas {ficha_jogador['nome']} jogou? "))

    for partida in range(ficha_jogador['partidas_jogadas']):
        gols = int(input(f"Quantos gols {ficha_jogador['nome']} fez na {partida + 1}° partida? "))
        gols_partidas.append(gols)

    ficha_jogador['gols_partidas'] = gols_partidas[:]
    ficha_jogador['total_gols'] = sum(gols_partidas)
    ficha_jogadores.append(ficha_jogador.copy())

    while continuar_parar not in "SN":
        continuar_parar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if continuar_parar == "N":
        break

print(f"{'cod':<4} {'nome':<15} {'gols':<15} {'total':<5}")
print("-" * 44)
for l, jogador in enumerate(ficha_jogadores):
    print(f"{l:<4} {jogador['nome']:<15} {str(jogador['gols_partidas']):<15} {jogador['total_gols']:<5}")

while True:
    opc = int(input("Quer ver os dados de qual jogador? "))
    if opc == 999:
        break
    if opc >= len(ficha_jogadores) or opc < 0:
        print(f"Erro! Não existe jogador com codigo {opc}! Tente novamente")
    else:
        print("-" * 34)
        print(f"Levantamento do jogador {ficha_jogadores[opc]['nome']}:")
        for i, g in enumerate(ficha_jogadores[opc]['gols_partidas']):
            print(f"  --> Na {i + 1}° partida {ficha_jogadores[opc]['nome']} fez {g} gols.")
            
print(f"<< VOLTE SEMPRE >>")