sexo = str(input("Qual o sexo da pessoa? [M/F]: ")).strip().upper()[0]

while sexo not in "MF": 
    sexo = str(input("sexo invalido! Informe o sexo da pessoa: ")).strip().upper()[0]
print(f"O sexo da pessoa é {sexo}, registrado com sucesso.")
