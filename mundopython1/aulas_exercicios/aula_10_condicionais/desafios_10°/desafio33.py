n1 = int(input("Qual é o primeiro número? "))
n2 = int(input("Qual é o segundo número? "))
n3 = int(input("Qual é o terceiro número? "))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
menor = n1  
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f"O maior número é {maior} e o menor é {menor}")