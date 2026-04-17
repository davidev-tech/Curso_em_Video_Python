escolher_cor = (
    '\033[m',          # 0 - Sem Cor
    '\033[0;30;41m',   # 1 - Vermelho
    '\033[0;30;42m',   # 2 - Verde
    '\033[0;30;43m',   # 3 - Amarelo
    '\033[0;30;44m',   # 4 - Azul
    '\033[7;30m'       # 5 - Branco (Invertido)
)


def exibir_titulo(msg, cor=0):
    """
    --> Exibe o Titulo formatado com bordas ajustaveis e cor.
    :param msg: Recebe com.
    :param cor: Recebe Índice numérico da cor desejada (conforme tupla escolher_cor).
    :return: Nenhum."""
    tam = len(msg) + 4

    print(escolher_cor[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(escolher_cor[0], end='')


def acessar_manual(com):
    """
    --> Acessar a função exibir_titulo para formatar o titulo e em seguida exibe o manual com cores.
    :param com: Recebe comando.
    :return: Nenhum."""
    exibir_titulo(f'Acessando o manual do comando \"{com}\"', 4)
    print(escolher_cor[5], end='')
    help(com)
    print(escolher_cor[0], end='')


# =============================================================================================
# DESAFIO 106: Personalizando a ajuda interativa usando funções.
# Objetivo: Criar funções mais interativas com cores e bordas, além de praticar encapsulamento,
# principio de responsabilidade unica.
# Conceitos: Encapsulamento de lógica, Principio de Responsabilidades Unicas.
# =============================================================================================

comando = ''
while True:
    exibir_titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input("Função ou Biblioteca > ")).strip()
    if comando.upper() == 'FIM':
        break
    else:
        acessar_manual(comando)