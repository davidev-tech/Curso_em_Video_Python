# =============================================================================================
# DESAFIO 112: Processar dados usando pacotes e modulos.
# Objetivo: Praticar Modularização, encapsulamento, principio de responsabilidade unica,
#sanitização dos dados.
# Conceitos: Modularização, Encapsulamento de lógica, Principio de Responsabilidades Unicas.
# =============================================================================================

from utilidades import moedas, dados

preco = dados.leia_dinheiro('Digite o preço do Produto: R$')
taxa_aumento = dados.leia_dinheiro('Digite qual será a taxa para o aumento do valor: ')
taxa_reduzir = dados.leia_dinheiro('Digite qual será a taxa para reduzir o valor: ')
formatar = False
valores_formatados = ' '

while valores_formatados not in 'SN':
    valores_formatados = str(input('Deseja os valores formatados? [S/N]: ')).strip().upper()[0]
formatar = (valores_formatados == 'S')
moedas.exibir_tabela(preco, taxa_aumento, taxa_reduzir, formatar)