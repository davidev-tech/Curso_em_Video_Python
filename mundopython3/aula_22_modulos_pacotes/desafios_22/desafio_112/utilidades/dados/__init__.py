def leia_dinheiro(msg):
    """
    --> Valida se a entrada é realmente um número decimal com uso de ponto ou virgula.
    :param msg: recebe preco.
    :return nenhum."""
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        
        if entrada.replace('.', '', 1).isdigit():
            valido = True
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')