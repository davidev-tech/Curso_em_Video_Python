def calcular_fatorial(num=1):
    """
    --> Calcula o fatorial de um número.
    :param num: recebe número int digitado pelo usuário para calcular seu fatorial.
    :return f: O resultado fatorial do calculo (int).
    """

    f = 1
    for c in range(num, 0, -1):
        f*= c
    return f


def exibir_fatorial(valor_fatorial, num=1, exibir_calculo = False):
    """
    --> Exibe o valor fatorial de um número, e caso o usuário queira, irá mostrar o calculo também.
    :param valor_fatorial: Resultado fatorial do número passado anteriormente
    :param num: valor passado anteriormente para calcular o fatorial.
    :param exibir_calculo: contem bool True ou False, para verificar se exibi ou não os calculos.
    :return: Nenhum retorno
    """
    from time import sleep

    if exibir_calculo:
        borda = (num + 2) * 2
        print("--" * borda)
        for c in range(num, 0, -1):
            sleep(1.2)
            print(f"{c}",'x' if c > 1 else '=' ,end=' ', flush=True)
    else:
        print("--" * 2)

    print(valor_fatorial)


# ==============================================================================
# DESAFIO 102: Função para Fatorial (Cálculo e Exibição)
# Objetivo: Implementar parâmetros opcionais e a "Camada de Tradução" (UX to Logic).
# Conceitos: Parâmetros booleanos, loops de cálculo e controle de verbosidade.
# ==============================================================================

processo = ' '
help(exibir_fatorial)
numero = int(input("Qual número deseja descobrir o fatorial? "))
while processo not in 'SN':
    processo = str(input("Deseja Visualizar o Processo? [S/N]: ")).upper().strip()[0]

exibir_processo = (processo == "S")
valor_fat = calcular_fatorial(numero)
exibir_fatorial(valor_fat, numero, exibir_processo)