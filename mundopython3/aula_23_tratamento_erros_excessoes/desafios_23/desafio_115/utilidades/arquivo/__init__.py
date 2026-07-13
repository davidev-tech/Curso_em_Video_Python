
from utilidades._interfaces_ import *

def verificar_existencia_arquivo(nome):
    try:
        a = open(nome, "rt") # -> dentro da função open passamos o nome do arquivo, seguida da ação.
        a.close()
    except FileNotFoundError:  # -> Exceção para quando o arquivo não é encontrado no local especificado.
        return False
    else: 
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print('ERRO ao ler o arquivo!')
    else:
        exibir_cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:3>} anos')
    finally:
        a.close()


def cadastrar_usuario(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de registrar os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()