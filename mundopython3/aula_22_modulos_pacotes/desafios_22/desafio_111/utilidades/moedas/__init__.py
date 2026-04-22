def calcular_metade_valor(n, formatar=False):
    """
    --> Calcula a Matade do valor.
    :param n: Recebe preco.
    :return resposta.
    """
    resposta = n / 2
    return formatar_preco(resposta) if formatar else resposta


def calcular_dobro_valor(n, formatar=False):
    """
    --> Calcula o dobro do valor.
    :param n: Recebe preco.
    :return resposta.
    """
    resposta = n * 2
    return formatar_preco(resposta) if formatar else resposta


def aumentar_porcentagem_valor(n=0, taxa=10, formatar=False):
    """
    --> Calcula o valor + taxa sobre o valor.
    :param n: Recebe preco.
    :param taxa: taxa_aumento.
    :return resposta."""
    valor_aumentado = taxa/100 * n
    resposta = n + valor_aumentado

    return formatar_preco(resposta) if formatar else resposta


def reduzir_porcentagem_valor(n=0, taxa=10, formatar=False):
    """
    --> Calcula o valor - taxa sobre o valor.
    :param n: Recebe preco.
    :param taxa: taxa_reduzir.
    :return resposta.
    """
    valor_redutor = taxa/100 * n
    resposta = n - valor_redutor

    return formatar_preco(resposta) if formatar else resposta


def formatar_preco(preco=0, simbolo_monetario="R$"):
    """
    Transforma um valor numérico em uma string formatada como moeda.
    :param preco: O valor numérico a ser formatado.
    :param simbolo_monetario: O símbolo da moeda (padrão R$).
    :return: String formatada com o símbolo e vírgula.
    """
    valor_ajustado = f'{preco:.2f}'.replace(".", ",")
    
    return f'{simbolo_monetario}{valor_ajustado}'


def exibir_tabela(preco=0, taxa_a=10, taxa_r=13, formatar= False):
    """
    --> Exibe os resultados em formato de tabela.
    :param preco: recebe preco.
    :param taxa_a: recebe taxa_aumento.
    :param taxa_r: recebe taxa_reduzida.
    :return nenhum."""

    print('-' * 36)
    print(f'{"RESUMO DO VALOR".center(36)}')
    print('-' * 36)

    print(f'Preço analisado: \t{formatar_preco(preco)}')
    print(f'Dobro do preço: \t{calcular_dobro_valor(preco, formatar)}')
    print(f'Metade do preço: \t{calcular_metade_valor(preco, formatar)}')

    desc_aumento = f'{taxa_a:.2f}% de aumento:'
    print(f'{desc_aumento} \t{aumentar_porcentagem_valor(preco, taxa_a, formatar)}')

    desc_reducao = f'{taxa_r:.2f}% de redução:'
    print(f'{desc_reducao} \t{reduzir_porcentagem_valor(preco, taxa_r, formatar)}')
    print('-' * 36)