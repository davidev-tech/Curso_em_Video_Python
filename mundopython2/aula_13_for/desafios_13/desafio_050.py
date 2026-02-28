soma = 0
numeros_pares = 0
for x in range(1, 7):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
        par = numeros
        numeros_pares += 1
        soma += par
print(f"Foram informados {numeros_pares} números pares.")
print(f"A somatorio dos números pares foi = {soma}")