soma = 0
impares_multiplos_tres = 0
print("Os números que são impares e multiplos de 3 entre 1 e 500 são: ")
print("-=-" * 15)
for x in range(1, 501, 2):
    if x % 3 == 0:
        print(f"O número {x} é impar e divisivel por 3.")
        soma += x
        impares_multiplos_tres += 1
print("FIM! LISTA!")
print("-=-" * 15)
print(f"{impares_multiplos_tres} números são impares, multiplos de 3.")
print(f"A soma entre todos esses números foi {soma}")