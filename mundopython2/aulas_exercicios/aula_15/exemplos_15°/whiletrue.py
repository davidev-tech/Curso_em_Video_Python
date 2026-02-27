numero = somatorio = 0
while True: # loop infinito.
    numero = int(input("Digite um número: "))
    if numero == 999:
        break # break interrompe o loop e sai dele. Nada que estiver estiver escrito depois do break irá ser lido.
    somatorio += numero
print(f"A soma dos números digitados foi: {somatorio}.")