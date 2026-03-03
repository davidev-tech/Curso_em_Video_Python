"""
Desafio 075: Análise estatística e mapeamento de frequências em Tuplas.
"""

indice = 1
numeros = (int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: ")),
int(input("Digite o quarto número: ")), int(input("Digite o quinto número: ")))
print("=" * 25)
print("Os valores informados foram: ")

for numero in numeros:
    print(f"{numero}", end=", " if indice < 5 else "")
    indice += 1

print("\n", "=" * 25)
print(f"O número 9 apareceu: {numeros.count(9)} Vezes.")
print("=" * 25)

if 3 in numeros:
    print(f"O número 3 apareceu no indice {numeros.index(3) + 1}.")
else:
    print("Não houve número 3 digitado.")

print("=" * 25)
print("Os números pares digitados foram:")

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero}", end=" ")