# =============================================================================================
# DESAFIO 107: Processar dados usando pacotes e modulos.
# Objetivo: Praticar Modularização, encapsulamento, principio de responsabilidade unica.
# Conceitos: Modularização, Encapsulamento de lógica, Principio de Responsabilidades Unicas.
# =============================================================================================

from processar_dados import moedas

preco = float(input('Digite o preço do Produto: R$'))
taxa_aumento = float(input('Digite qual será a taxa para o aumento do valor: '))
taxa_reduzir = float(input('Digite qual será a taxa para reduzir o valor: '))
print(f'A metade de {(preco)} é {moedas.calcular_metade_valor(preco)} Reais')
print(f'O dobro de {(preco)} é {moedas.calcular_dobro_valor(preco)} Reais')
print(f'O preco de {(preco)} aumentado em {taxa_aumento}% é {moedas.aumentar_porcentagem_valor(preco, taxa_aumento)} Reais.')
print(f'O preco de {(preco)} reduzido em {taxa_reduzir}% é {moedas.reduzir_porcentagem_valor(preco, taxa_reduzir)} Reais.')