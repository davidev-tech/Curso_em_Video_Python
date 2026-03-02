soma_idade = 0
idade_homen_mais_velho = 0
mulheres_menos_20_anos = 0
pessoas_registradas = 0
nome_homem_mais_velho = ""

for x in range(0, 4):
    print(f"------ {x + 1}° PESSOA -----")
    nome = str(input("Qual o nome da Pessoa? ")).strip()
    idade = int(input("Qual a idade da Pessoa? "))
    sexo = int(input("""Qual o sexo da Pessoa:
[ 1 ] Homem
[ 2 ] Mulher
Respota: """))
    soma_idade += idade
    if sexo == 1:
        if idade_homen_mais_velho == 0:
            idade_homen_mais_velho = idade
            nome_homem_mais_velho = nome
        elif idade > idade_homen_mais_velho:
            idade_homen_mais_velho = idade
            nome_homem_mais_velho = nome
    elif sexo == 2:
        if idade < 20:
            mulheres_menos_20_anos += 1
    else:
        print("OPÇÃO INVALIDA!")
    pessoas_registradas += 1  
if pessoas_registradas == 0:
    print("Não houve pessoas registradas.")
else:    
    media_idade = soma_idade / 4
    print(f"A media de idade do grupo foi de: {media_idade} anos.")
    print(f"O nome do homem mais velho foi {nome_homem_mais_velho} com {idade_homen_mais_velho} anos.")
    print(f"A quantidade de mulheres com menos de 20 anos registradas foi de {mulheres_menos_20_anos} mulheres.")