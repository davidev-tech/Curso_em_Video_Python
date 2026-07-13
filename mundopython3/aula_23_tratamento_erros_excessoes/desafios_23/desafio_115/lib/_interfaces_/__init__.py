def linha(tam = 40):
    print('-' * tam)


def exibir_cabecalho(msg):
    linha()
    print(f'{msg.center(40)}')
    linha()

    
def exibir_menu():
    lista_opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']
    exibir_cabecalho("MENU PRINCIPAL")
    c = 1
    for opc in lista_opcoes:
        print(f'\033[33m{c}\033[m - \033[34m{opc}\033[m')
        c += 1
    linha()


def escolher_cores(opcao_cor=0):
    escolher_cor = (
    '\033[m',          # 0 - Sem Cor
    '\033[0;30;41m',   # 1 - Vermelho
    '\033[0;30;42m',   # 2 - Verde
    '\033[0;30;43m',   # 3 - Amarelo
    '\033[0;30;44m',   # 4 - Azul
    '\033[7;30m'       # 5 - Branco (Invertido)
                   )
    return escolher_cor