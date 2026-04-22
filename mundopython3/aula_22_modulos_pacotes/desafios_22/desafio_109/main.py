# =============================================================================================
# DESAFIO 109: Processar dados usando modulo.
# Objetivo: Praticar Modularização, encapsulamento, principio de responsabilidade unica.
# Conceitos: Modularização, Encapsulamento de lógica, Principio de Responsabilidades Unicas.
# =============================================================================================

import moedas

preco = float(input('Digite o preço do Produto: R$'))
taxa_aumento = float(input('Digite qual será a taxa para o aumento do valor: '))
taxa_reduzir = float(input('Digite qual será a taxa para reduzir o valor: '))
formatar = False
valores_formatados = ' '
while valores_formatados not in 'SN':
    valores_formatados = str(input('Deseja os valores formatados? [S/N]: ')).strip().upper()[0]
    formatar = (valores_formatados == 'S')
print(f'A metade de {moedas.formatar_preco(preco)} é {moedas.calcular_metade_valor(preco, formatar)}')
print(f'O dobro de {moedas.formatar_preco(preco)} é {moedas.calcular_dobro_valor(preco, formatar)}')
print(f'O preco de {moedas.formatar_preco(preco)} aumentado em {taxa_aumento}% é {moedas.aumentar_porcentagem_valor(preco, taxa_aumento, formatar)}')
print(f'O preco de {moedas.formatar_preco(preco)} reduzido em {taxa_reduzir}% é {moedas.reduzir_porcentagem_valor(preco, taxa_reduzir, formatar)}')