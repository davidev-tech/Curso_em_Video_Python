def calcular_metade_valor(n=0):
    """
    --> Calcula a Matade do valor.
    :param n: Recebe preco.
    :return resposta.
    """
    resposta = n / 2
    return resposta


def calcular_dobro_valor(n=0):
    """
    --> Calcula o dobro do valor.
    :param n: Recebe preco.
    :return resposta
    """
    resposta = n * 2
    return resposta


def aumentar_porcentagem_valor(n=0, taxa=10):
    """
    --> Calcula o valor + taxa sobre o valor.
    :param n: Recebe preco.
    :param taxa: taxa_aumento.
    :return resposta
    """
    valor_aumentado = taxa/100 * n
    resposta = n + valor_aumentado

    return resposta


def reduzir_porcentagem_valor(n=0, taxa=10):
    """
    --> Calcula o valor - taxa sobre o valor.
    :param n: Recebe preco.
    :param taxa: taxa_reduzir.
    :return resposta
    """
    valor_redutor = taxa/100 * n
    resposta = n - valor_redutor

    return resposta