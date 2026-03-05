"""
Desafio 081: Análise quantitativa e qualitativa de dados em Listas dinâmicas.
"""

numeros = []

while True:
    continuar_parar = " "
    numeros.append(int(input("Digite um numero: ")))
    
    while continuar_parar not in "SN":
        continuar_parar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar_parar in "N":
        break

numeros.sort(reverse=True)
print(f"A lista contem {len(numeros)} números.")
print(f"A lista em ordem decrescente {numeros}")

if 5 not in numeros:
    print("A lista não contêm o número 5.")
else:
    print(f"A lista tem o número 5 e se encontra no indice {numeros.index(5) + 1}")