from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

for x in range(0, 7):
    nascimento = int(input("Em que ano o cidadão nasceu? "))
    idade = ano_atual - nascimento
    if idade < 0:
        print("IDADE INVALIDA!")
    else:
        if idade < 18:
            menor_idade += 1
        else:
            maior_idade += 1

print(f"{maior_idade} Pessoas são maiores de idade.")
print(f"{menor_idade} Pessoas são menores de idade.")