pessoas = []
dados = []
total_maior = total_menor = 0

for contador in range(0,3):
    dados.append(str(input("Qual o nome da pessoa? ")))
    dados.append(int(input("Qual a idade da pessoa? ")))
    pessoas.append(dados[:])
    dados.clear()

for p in pessoas:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade.")
        total_maior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        total_menor += 1

print(f"Temos {total_maior} maiores e {total_menor} menores.")