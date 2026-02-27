pessoas_cadastradas = 0
pessoas_cadastradas_18_mais = 0
homens_cadastrados = 0
mulheres_menos_20_anos = 0
sexo = ""
continuar_parar = ""
idade = -1
print("-" * 25)
print("   CADASTRE UMA PESSOA   ")
print("-" * 25)
while True:
        while sexo not in "MF": # Bindagem dos dados em sexo.
            sexo = str(input("Qual o sexo da pessoa? Masculino ou Feminino. [MF] ")).strip().upper()[0]
        while idade < 0 or idade > 120: # Blindagem dos dados em idade
            idade = int(input("Qual a idade da pessoa? "))
        if idade <= 18:
            pessoas_cadastradas += 1
        else:
             pessoas_cadastradas_18_mais +=1  
        if sexo == "M":
            homens_cadastrados += 1
        elif sexo == "F":
            if idade < 20:
                mulheres_menos_20_anos += 1
        while continuar_parar not in "CP": # Blindagem dos dados de parada.
            continuar_parar = str(input("Deseja Continuar ou Parar? [C/P]")).strip().upper()[0] 
            print("-" * 25)
            print("   CADASTRE UMA PESSOA   ") 
            print("-" * 25)
        if continuar_parar == "P":
            break
        sexo = ""
        continuar_parar = ""
        idade = -1
print("-" * 30)
print(f"{pessoas_cadastradas} Pessoas foram cadastradas.")
print(f"{pessoas_cadastradas_18_mais} Pessoas com mais de 18 anos foram cadastradas.")
print(f"{homens_cadastrados} Homens foram cadastrados.")
print(f"{mulheres_menos_20_anos} Mulheres com menos de 20 anos foram cadastradas.")