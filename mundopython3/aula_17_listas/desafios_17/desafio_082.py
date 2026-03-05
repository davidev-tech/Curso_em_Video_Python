"""
Desafio 082: Processamento de dados em listas dinâmicas com filtragem e derivação de subconjuntos (Pares e Ímpares).
"""
valores = []
valores_pares = []
valores_impares = []

while True:
    continuar_parar = " "
    valores.append(int(input("Digite um número: ")))
    while continuar_parar not in "SN":
        continuar_parar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar_parar in "N":
        break

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

print(f"-=-" * 30)
print(f"A lista completa do números digitados: {valores}")
print(f"-=-" * 30)
print(f"A lista somente com os números pares: {valores_pares}")
print(f"-=-" * 30)
print(f"A lista somente com os números impares: {valores_impares}")
print(f"-=-" * 30)