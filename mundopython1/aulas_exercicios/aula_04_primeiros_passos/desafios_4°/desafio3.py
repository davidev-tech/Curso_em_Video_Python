numero1 = (input("Digite o primeiro número: "))
numero2 = (input("Digite o segundo número: "))
soma = numero1 + numero2
print(f"A soma entre {numero1} e {numero2} é igual a {soma}")
# O código acima não funciona, pois o input retorna uma string. Para corrigir isso, precisamos converter os inputs para números inteiros usando a função int().