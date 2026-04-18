def calcular_metade_valor(n):
    """
    --> Calcula a Matade do valor.
    :param n: Recebe preco.
    :return n/2
    """
    return n / 2


def calcular_dobro_valor(n):
    """
    --> Calcula o dobro do valor.
    :param n: Recebe preco.
    :return n*2
    """
    return n * 2


def aumentar_porcentagem_valor(n=0, taxa=10):
    """
    --> Calcula o valor + taxa sobre o valor.
    :param n: Recebe preco.
    :param taxa: taxa_aumento.
    :return n"""
    valor_aumentado = taxa/100 * n
    n += valor_aumentado

    return n


def reduzir_porcentagem_valor(n=0, taxa=10):
    """
    --> Calcula o valor - taxa sobre o valor.
    :param n: Recebe preco.
    :param taxa: taxa_reduzir.
    :return n
    """
    valor_redutor = taxa/100 * n
    n -= valor_redutor

    return n


def formatar_preco(preco=0, simbolo_monetario="R$"):
    """
    Transforma um valor numérico em uma string formatada como moeda.
    :param preco: O valor numérico a ser formatado.
    :param simbolo_monetario: O símbolo da moeda (padrão R$).
    :return: String formatada com o símbolo e vírgula.
    """
    valor_ajustado = f'{preco:.2f}'.replace(".", ",")
    
    return f'{simbolo_monetario}{valor_ajustado}'