somatorio = 0
numeros_digitados = 0
numero = int(input('Digite um número [999 para parar]: '))

while numero != 999: # verifica a entrada antes de realizar as operações. É o while com flag, a bandeira de pare.
    numeros_digitados += 1
    somatorio += numero   # Ele realiza as operações da primeira entrada.
    numero = int(input("Digite um número: "))  
print(f"{numeros_digitados} foram digitados.") 
print(f"A soma dos números digitados foi: {somatorio}")