from lib._interfaces_ import *
from lib.tratar_dados import *
from lib.arquivo import *
from time import sleep

arq = 'cadastro_usuarios.txt'

if not verificar_existencia_arquivo(arq):
    criar_arquivo(arq)

opcoes = [1, 2, 3]

while True:
    exibir_menu()
    opcao = tratar_opcoes(opcoes)

    if opcao == 3:
        linha()
        print('Saindo do sistema... Até logo!')
        linha()
        sleep(2)
        break

    if opcao == 1:
        lerArquivo(arq)
    else:
        exibir_cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = tratar_numero_inteiro('Idade: ')
        cadastrar_usuario(arq, nome, idade)
