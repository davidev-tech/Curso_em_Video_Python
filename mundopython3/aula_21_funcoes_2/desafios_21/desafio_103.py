def analisar_ficha(jogador='<desconhecido>', gols = 0):
    """
    --> Exibe os dados tratados.
    :param jogador: Recebe o nome do Jogador.
    :param gols: Recebe a quantidade de gols do Jogador.
    :return: Nenhum Retorno """
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")


# ==============================================================================
# DESAFIO 103: Ficha do Jogador (Sanitização de Dados)
# Objetivo: Lidar com dados omissos e validar tipos primitivos via Strings.
# Conceitos: .isnumeric(), .strip(), Parâmetros Opcionais e Programação Defensiva.
# ==============================================================================

print("--" * 16)
nome_jogador = str(input("Nome do jogador: ")).strip()
gols_digitados = str(input("Números de gols: ")).strip()
if gols_digitados.isnumeric():
    quantidade_gols = int(gols_digitados)
else:
    quantidade_gols = 0

if nome_jogador == '':
    analisar_ficha(gols=quantidade_gols)
else:
    analisar_ficha(nome_jogador,quantidade_gols)