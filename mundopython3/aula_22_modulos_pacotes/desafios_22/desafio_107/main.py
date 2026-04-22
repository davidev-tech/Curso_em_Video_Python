# =============================================================================================
# DESAFIO 107: Processar dados usando modulo.
# Objetivo: Praticar Modularização, encapsulamento, principio de responsabilidade unica.
# Conceitos: Modularização, Encapsulamento de lógica, Principio de Responsabilidades Unicas.
# =============================================================================================

import moedas

preco = float(input('Digite o preço do Produto: R$'))
taxa_aumento = float(input('Digite qual será a taxa para o aumento do valor: '))
taxa_reduzir = float(input('Digite qual será a taxa para reduzir o valor: '))
print(f'A metade de {(preco)} é R${moedas.calcular_metade_valor(preco)}')
print(f'O dobro de {(preco)} é R${moedas.calcular_dobro_valor(preco)}')
print(f'O preco de {(preco)} aumentado em {taxa_aumento}% é R${moedas.aumentar_porcentagem_valor(preco, taxa_aumento)}')
print(f'O preco de {(preco)} reduzido em {taxa_reduzir}% é R${moedas.reduzir_porcentagem_valor(preco, taxa_reduzir)}')