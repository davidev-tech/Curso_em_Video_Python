def tratar_dados():
    """
    --> Trata a entrada, obrigando que o return para o programa principal seja um (int)
    :param: Nenhum Parametro.
    :return numero: O valor inteiro para o programa principal"""
    while True:
        num = str(input("Digite um número inteiro: ")).strip()
        if num.isnumeric():
            numero = int(num)
            break
        else:
            print("ERRO! Digite um número inteiro válido.")

    return numero


# ==============================================================================
# DESAFIO 103: Ficha do Jogador (Sanitização de Dados)
# Objetivo: Lidar com dados omissos e validar tipos primitivos via Strings.
# Conceitos: .isnumeric(), .strip(), Parâmetros Opcionais e Programação Defensiva.
# ==============================================================================

def exibir_dados(num):
    """
    --> Exibe o valor que foi informado.
    :param num: Recebe n como parametro.
    :return: Nenhum retorno."""
    print(f"Você informou o número {num}")


n = tratar_dados()
exibir_dados(n)