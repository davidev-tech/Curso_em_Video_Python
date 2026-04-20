# =============================================================================================
# DESAFIO 110: Processar dados usando pacotes e modulos.
# Objetivo: Praticar Modularização, encapsulamento, principio de responsabilidade unica.
# Conceitos: Modularização, Encapsulamento de lógica, Principio de Responsabilidades Unicas.
# =============================================================================================

from processar_dados import moedas

preco = float(input('Digite o preço do Produto: R$'))
taxa_aumento = float(input('Digite qual será a taxa para o aumento do valor: '))
taxa_reduzir = float(input('Digite qual será a taxa para reduzir o valor: '))
formatar = False
valores_formatados = ' '

while valores_formatados not in 'SN':
    valores_formatados = str(input('Deseja os valores formatados? [S/N]: ')).strip().upper()[0]
formatar = (valores_formatados == 'S')

moedas.exibir_tabela(preco, taxa_aumento, taxa_reduzir, formatar)