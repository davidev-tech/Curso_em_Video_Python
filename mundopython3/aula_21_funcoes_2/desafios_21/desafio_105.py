def eh_float(valor):
    """
    --> Valida se uma string pode ser convertida para float, tratando pontos e vírgulas.
    """
    v = valor.strip().replace(',', '.')
    # Verifica se tem no máximo um ponto e se o resto é numérico
    return v.count('.') <= 1 and v.replace('.', '', 1).isnumeric()


def adicionar_notas():
    """
    --> Recebe entradas que serão validadas se são númericas. Caso sim, converte de str para float e verifica se o valor passado
    não é negativo ou superior a 10, em seguida caso esteja tudo ok, adicionar o valor a lista (notas).
    :param: Nenhum
    :return notas: Lista que contém todas as notas que passaram pelos testes, passadas pelo usuário.
    """
    notas = []

    print('--' * 20)
    while True:
        nota_entrada = str(input('Digite a nota: ')).strip()
        nota_valida = False
        
        if eh_float(nota_entrada):
            n = float(nota_entrada.replace(',', '.'))
            if n >= 0 and n <= 10:
                nota_valida = True
                notas.append(n)
            else:
                print('A nota não pode ser inferior a 0 e nem superior a 10.')
        else:
            print(f'ERRO! A nota Precisa ser um número inteiro ou decimail e não pode ter mais de 1 ponto ou virgula.')
    

        if nota_valida == True: 
            while True:
                entrada = str(input('Deseja continuar a adicionar notas? [S/N]: ')).strip().upper()
                if entrada in('S','N'): 
                    continuar_parar = (entrada == 'S')
                    if continuar_parar == True:
                        break
                    else:
                        print('--' * 20)
                        return notas
                else:
                    print('ERRO! Responda apenas S ou N.')   


def processar_notas(*n):
    """
    --> Processa os valores que estavam dentro da lista colocando cada valor individualmente na tupla, funções como:
    len(), max(), min(), sum() foram usadas para processar os dados e em seguida esses dados processados foram
    guardados em um dicionario.
    :param *n: Faz o empacotamento dos valores da lista notas_alunos que realizou o desempacotamento.
    :return alunos: Dicionario criado localmente para armazenar todos esses dados  e ser enviado para um dicionario
    global registro_alunos.
    """
    alunos = {}
    alunos["notas"] = n
    alunos["quantidade_notas"] = len(n)
    alunos["maior_nota"] = max(n)
    alunos["menor_nota"] = min(n)
    if alunos['quantidade_notas'] >= 1:
        alunos["media_notas"] = sum(n) / alunos["quantidade_notas"]

    return alunos


def exibir_situacao():
    """
    --> Verifica se o o usuário quer ver a situação dos alunos retornando um valor True ou False.
    :param: Nenhum.
    :return situacao_geral: Um Valor True ou False. 
    """
    situacao_geral = False

    while True:
        situacao_entrada = str(input('Deseja ver a situação geral? [S/N]: ')).strip().upper()
        if situacao_entrada in ('S','N'):
            situacao_geral = (situacao_entrada == 'S')
            break
        print('ERRO! Responda apenas S ou N.')
    
    return situacao_geral


def verificar_situacao_geral(dic_alunos, situacao_geral=False):
    """
    --> Verifica a media das notas e retorna um valor que condiz com aquela média.
    :param dic_alunos: Recebe o dicionario registro_alunos
    :param situacao_geral: Recebe exibir_situacao_geral a resposta do usuário se deseja ou não ver a situação geral.
    :return dic["situação_geral"]: Chave ["situação_geral"] e um valor (str) escrito 'RUIM', 'RAZOÁVEL' OU 'BOA'
    """
    if situacao_geral == True:
            if dic_alunos["media_notas"] < 6:
                dic_alunos["situação_geral"] = 'RUIM'
            elif dic_alunos["media_notas"] < 7:
                dic_alunos["situação_geral"] = 'RAZOÁVEL'
            else:
                dic_alunos["situação_geral"] = 'BOA'

    return dic_alunos["situação_geral"]


def exibir_registro_alunos(reg_alunos,situacao=False):
    """
    --> Exibe todos os dados registrados de forma organizada.
    :param reg_alunos: Recebe registro_alunos
    :param situacao: Recebe exibir_situacao_geral, caso True exibe, caso contrario, não.
    :return: Nenhum.
    """
    print('-=-' * 16)
    print(f'{"Dados Registrados".center(48)}')
    print('-=-' * 16)
    print(f'A quantidade de notas registradas foram: {reg_alunos["quantidade_notas"]} notas.')
    print(f'A maior nota registrada foi: {reg_alunos["maior_nota"]}')
    print(f'A menor nota registrada foi: {reg_alunos["menor_nota"]}')
    print(f'A media das notas registradas foi: {reg_alunos["media_notas"]:.1f}')
    if situacao:
        print(f'A situação geral foi: {reg_alunos["situação_geral"]}.')
    
    
# =============================================================================================
# DESAFIO 105: Validando dados com Principio de responsabilidade unica e tratando.
# Objetivo: Criar funções de leitura robostas, com loop infinito e tecnicas para 
# validação de dados, além de praticar encapsulamento e principio de responsabilidade unica.
# Conceitos: Encapsulamento de lógica, sanitização na borda e controle de fluxo
# Principio de Responsabilidades Unicas.
# =============================================================================================

notas_alunos = adicionar_notas()
registro_alunos = processar_notas(*notas_alunos)
exibir_situacao_geral = exibir_situacao()

if exibir_situacao_geral == True:
    registro_alunos['situação_geral'] = verificar_situacao_geral(registro_alunos, True)

exibir_registro_alunos(registro_alunos, exibir_situacao_geral)