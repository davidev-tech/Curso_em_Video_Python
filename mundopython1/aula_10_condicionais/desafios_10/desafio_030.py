from time import sleep
numero = int(input("Digite um número inteiro: "))
print("PROCESSANDO...")
sleep(3)
if numero%2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é impar!")