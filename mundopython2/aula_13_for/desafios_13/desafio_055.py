maior_peso = 0
menor_peso = 0

for x in range(0, 5):
    peso = float(input(f"Qual o peso da {x + 1}° Pessoa? "))
    if x == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
            
print(f"O Maior Peso lido foi: {maior_peso:.1f} kg.")
print(f"O Menor Peso lido foi: {menor_peso:.1f} kg.")