num = 1
pares = 0
impares = 0
while num != 0:
    num = int(input("Digite um valor: "))
    if num != 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f"{pares} números eram pares.")
print(f"{impares} números eram impares.")