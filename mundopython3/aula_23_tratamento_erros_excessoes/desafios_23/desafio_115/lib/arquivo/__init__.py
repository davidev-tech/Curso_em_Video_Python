from lib._interfaces_ import *

def verificar_existencia_arquivo(nome):
    """
    --> Verifica se o arquivo existe.
    :param nome.
    :return True ou False.
    """
    try:
        a = open(nome, "rt") # -> dentro da função open passamos o nome do arquivo, seguida da ação.
        a.close()
    except FileNotFoundError:  # -> Exceção para quando o arquivo não é encontrado no local especificado.
        return False
    else: 
        return True


def criar_arquivo(nome):
    """
    --> Tenta criar o arquivo.
    :param nome.
    :return mensagem informando se deu certo ou não.
    """
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    """
    --> Tenta ler o arquivo.
    :param nome.
    :return mensagem informando as pessoas cadastradas. Em casos de erro, informa que houve um erro ao ler o arquivo .
    """
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
    """
    --> Tenta cadastrar um novo usuário.
    :param arq, nome='desconhecido', idade=0.
    :return mensagem informando se houve algum erro seja na abertura do arquivo ou ao registrar os dados, ou se deu tudo certo.
    """
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
