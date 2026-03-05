numero = somatorio = 0
numero_digitados = 0

while True:
    numero = int(input("Digite um valor: "))
    if numero == 999:
        break
    
    somatorio += numero
    numero_digitados += 1
    
print(f"A soma dos {numero_digitados} números digitados foi: {somatorio}.")