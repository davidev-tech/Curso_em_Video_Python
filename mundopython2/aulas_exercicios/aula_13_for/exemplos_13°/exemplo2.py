inicio = int(input("Qual o primeiro número?  "))
fim = int(input("Qual o ultimo número? "))
passo = int(input("Qual o valor do salto? "))

for x in range(inicio, fim + 1, passo):
    print(x)
print("FIM!")