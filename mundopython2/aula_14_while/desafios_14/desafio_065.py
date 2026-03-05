resposta = "S"
somatorio = 0
numero = int(input("Digite um número: "))
somatorio = numero
maior = numero
menor = numero
numeros_digitados = 1
resposta = str(input("Deseja continuar? [S/N]: ")).upper()[0]

if resposta == "S":
    while resposta == "S":    
        numero = int(input("Digite um número: "))
        somatorio += numero
        numeros_digitados += 1
        
        resposta = str(input("Deseja continuar? [S/N]: ")).upper()[0]
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media_numeros_digitados = somatorio / numeros_digitados

print(f"A média de todos os valores lidos foi: {media_numeros_digitados}.")
print(f"O maior número lido foi: {maior}.")
print(f"O menor número lido foi: {menor}.")
print(f"A soma dos números lidos foi: {somatorio}.")