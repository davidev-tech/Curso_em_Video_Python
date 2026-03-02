from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Informe o seu ano de nascimento? "))
idade = ano_atual - ano_nascimento
idade_alistamento = 18

if idade < 18:
    tempo_faltante_alistamento = idade_alistamento - idade
    print(f"Com {idade} anos, faltam {tempo_faltante_alistamento} anos para o seu alistamento obrigatório.")
    tempo = idade - 18
    futuro_alistamento = ano_atual + tempo
    print(f"Seu alistamento será em {futuro_alistamento}.")
elif idade > 18:
    tempo_perdido_alistamento = idade - idade_alistamento
    print(f"Com {idade} anos, você está {tempo_perdido_alistamento} anos atrasado para o alistamento.")
    print("Você deve comparecer imediatamente para o alistamento militar.")
    tempo = idade - 18
    ano_alistamento = ano_atual - tempo
else:
    print(f"Você chegou aos {idade} anos. Deve comparecer a junta militar para o alistamento imediato.")