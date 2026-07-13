def tratar_numero_inteiro():
    """
    --> Trata a entrada, até que seja um número inteiro.
    :param nenhum.
    :return numero_int.
    """
    while True:
        try:
            numero_int = int(input('\033[0;36mDigite um número inteiro: \033[m'))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um número do tipo inteiro.\033[m')
        except KeyboardInterrupt:
            print('\033[0;33mERRO! Valor não informado.\033[m')
            return 0
        else:
            return numero_int
        

def tratar_numero_real():
    """
    --> Trata a entrada, até que seja um número real.
    :param nenhum.
    :return numero_real.
    """
    while True:
        try:
            numero_real = float(input('\033[0;36mDigite um número real: \033[m'))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um número do tipo real.\033[m')
        except KeyboardInterrupt:
            print('\033[0;33mERRO! Valor não informado.\033[m')
            return 0
        else:
            return numero_real