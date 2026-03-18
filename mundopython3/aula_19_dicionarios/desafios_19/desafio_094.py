"""
Desafio 094: Cadastro de Grupo com Dicionários e Listas.
Implementação de banco de dados volátil utilizando Lista de Dicionários.
Análise estatística de média de idade e filtragem seletiva por sexo e performance.
"""
pessoas_cadastradas = []
cadastro_pessoas = {}
total_idade = 0

while True:
    cadastro_pessoas.clear()
    continuar_parar = " "
    cadastro_pessoas['sexo'] = " "
    cadastro_pessoas['idade'] = -1

    cadastro_pessoas['nome'] = str(input("Qual o nome da pessoa? ")).strip()
    while cadastro_pessoas['sexo'] not in "MF":
        cadastro_pessoas['sexo'] = str(input("Qual o sexo da pessoa? [M/F]: ")).strip().upper()[0]
    while cadastro_pessoas['idade'] < 0 or cadastro_pessoas['idade'] > 120:
        cadastro_pessoas['idade'] = int(input("Qual a idade? "))  
    pessoas_cadastradas.append(cadastro_pessoas.copy())  

    while continuar_parar not in "SN":
        continuar_parar = str(input("Deseja continuar ou parar? [S/N]: ")).strip().upper()[0]
    if continuar_parar == "N":
        break
   
print(f"A) {len(pessoas_cadastradas)} pessoas foram cadastradas.")
for pessoa in pessoas_cadastradas: 
    total_idade += pessoa['idade']
 
media_idade = total_idade / len(pessoas_cadastradas)
print(f"B) A idade media das pessoas cadastradas é {media_idade:.2f}")

print("C) As mulheres cadastradas foram:", end= ' ')
for pessoa in pessoas_cadastradas: 
    if pessoa['sexo'] == 'F':
        print(f"{pessoa}", end=' ')
print()

print("D) As pessoas com a idade maior que a idade média do grupo foram: ")
for pessoa in pessoas_cadastradas:
    if pessoa['idade'] > media_idade:
        print(f"{pessoa['nome']} tem {pessoa['idade']} idade maior que a média idade do grupo.")