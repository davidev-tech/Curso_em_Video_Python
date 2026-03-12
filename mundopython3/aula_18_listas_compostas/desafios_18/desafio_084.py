"""
Desafio 084: Gerenciamento de matrizes (listas de listas) para auditoria de peso e volumetria de dados.
"""
pessoas = []
dados = []
maior_peso = menor_peso = 0

while True:
    continuar_parar = " "
    dados.append(str(input("Digite o nome: "))).strip()
    dados.append(float(input("Digite o Peso da pessoa: ")))
    
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    while continuar_parar not in "SN":
        continuar_parar = str(input("Deseja continuar ou parar? [S/N]: ")).strip().upper()[0]
    if "N" in continuar_parar:
        break

print("-=-" * 20)
print(f"Ao todo você cadastrou {len(pessoas)} Pessoas.")
print(f"O maior peso registrado foi de {maior_peso}kg. Peso que pertece:", end=" ")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"{p[0]}.")
print()

print(f"O menor peso registrado foi de {menor_peso}kg", end=" ")  
for p in pessoas:
    if p[1] == menor_peso:
        print(f"Peso que pertece: {p[0]}.")
print()