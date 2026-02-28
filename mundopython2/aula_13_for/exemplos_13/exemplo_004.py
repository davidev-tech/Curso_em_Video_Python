soma = 0 # Variavel acumulativa.
for x in range(0, 4):
    num = int(input("Digite um número: "))
    #soma = soma + num é a mesma coisa de soma +=num.
    soma += num
print(f"O somatorio entre todos os valores foi: {soma}")
print("FIM!")