"""
Desafio Bônus: Encapsulamento de Dados em Dicionários.
Interação Complexa: Manipulação de Múltiplas Chaves em um Objeto Mutável.
Simulação de Estado de Objeto: Centralização de Atributos (Padrão POO/Java).
"""

from random import randint
from time import sleep


def sortear_numeros(dados):
    '''Sorteando 5 valores aleatorios de 1 a 30'''
    for i in range(0, 5):
        dados['valores'].append(randint(1, 30))
    dados['maior'] = max(dados['valores'])
   

def somar_pares(dados):
    '''Buscando os números pares e a soma deles.'''
    for numero in dados['valores']:
        if numero % 2 == 0:
            dados['soma_pares'] += numero


def exibir_resultados(dados):
    """Exibe o relatório final de forma formatada e amigável."""
    print("-=" * 30)
    print("RESUMO DO PROCESSAMENTO".center(60))
    print("-=" * 30)
    
    print("Sorteando valores da lista:", end=' ', flush=True)
    for valor in dados['valores']:
        sleep(0.5)
        print(f"{valor}", end=' ', flush=True)
    print()
    print(f"O maior valor fornecido foi: {dados['maior']}")
    print(f"A soma de todos os valores pares foi: {dados['soma_pares']}")


relatorio = {
    'valores': [],
    'maior': 0,
    'soma_pares': 0
}

sortear_numeros(relatorio)
somar_pares(relatorio)
exibir_resultados(relatorio)