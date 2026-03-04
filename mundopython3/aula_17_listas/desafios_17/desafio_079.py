"""
Desafio 079: Gerenciamento de coleções com restrição de duplicidade e ordenação ascendente.
"""

numeros = []

while True:
    parar_continuar = " "
    numero = int(input("Digite um número: "))

    if numero not in numeros:
        numeros.append(numero)
    else:
        print(f"Não adicionaremos o número {numero}. Pois ele ja existe na lista.")
    while parar_continuar not in "SN":
        parar_continuar = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]

    if parar_continuar == "N":
        break

print("-=-" * 30)
print(f"Os números da lista são: {sorted(numeros)}")
print("-=-" * 30)