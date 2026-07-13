import urllib.request
import urllib.error


def check_site(url):
    """ Verifica se a conexão da url está funcionando normalmente.
    :param url
    :return um texto dizendo se está acessivel ou não.
    """
    try:
        site = urllib.request.urlopen(url, timeout=5)
    except urllib.error.URLError:
        print(f'\033[31mO site {url} não está acessível no momento.\033[m')
    except Exception as erro:
        print(f'\033[31mOcorreu um erro inesperado: {erro.__class__}\033[m')
    else:
        print(f'\033[32mConsegui acessar o site {url} com sucesso!\033[m')