pessoas = []
dados = []
for contador in range(0,3):
    dados.append(str(input("Qual o nome da pessoa? ")))
    dados.append(int(input("Qual a idade da pessoa? ")))
    pessoas.append(dados[:])
    dados.clear()

print(pessoas)