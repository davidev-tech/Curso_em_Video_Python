def analisar_ficha(jogador='desconhecido', gols = 0):
    """
    --> Exibe os dados tratados.
    :param jogador: Recebe o nome do Jogador.
    :param gols: Recebe a quantidade de gols do Jogador.
    :return: Nenhum Retorno """
    print(f"O Jogador {jogador} fez {gols} gols.")


nome_jogador = str(input("Qual o nome do jogador? ")).strip()
gols_digitados = str(input("Quantos gols o jogador fez? ")).strip()
if gols_digitados.isnumeric():
    quantidade_gols = int(gols_digitados)
else:
    quantidade_gols = 0

if nome_jogador == '':
    analisar_ficha(gols=quantidade_gols)
else:
    analisar_ficha(nome_jogador,quantidade_gols)