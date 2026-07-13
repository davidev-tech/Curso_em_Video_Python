def tratar_numero_inteiro(msg):
    """
    --> Trata a entrada, até que seja um número inteiro.
    :param nenhum.
    :return numero_int.
    """
    while True:
        try:
            numero_int = int(input(f'\033[32m{msg}\033[m'))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! A entrada deve ser um número do tipo inteiro\033[m')
        except KeyboardInterrupt:
            print('\033[0;3mERRO! Valor não informado.\033[m')
        else:
            return numero_int
        

def tratar_opcoes(lista_opcoes_validas):
    """
    --> Trata a entrada, até que seja um número inteiro.
    :param nenhum.
    :return uma lista das opções validas: 1, 2 ou 3.
    """
    while True:
        resp = tratar_numero_inteiro(('\033[32mOpção escolhida: \033[m'))
        if resp in lista_opcoes_validas:    
            return resp
        print(f'\033[31mERRO! Escolha uma opção válida {lista_opcoes_validas}.\033[m')