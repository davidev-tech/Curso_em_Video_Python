n1 = int (input("Informe o primeiro número: "))
n2= int (input("Informe o segundo número: "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
potencia = n1 ** n2
resto = n1 % n2

print(f"\nA soma dos números é igual {soma}.\nA subtração é igual {sub}.\nA multiplicação é igual {mult}.\nA divisão é igual {div:.3f}.")
# :numf determina a quantidade de pontos flutuantes.
# end= ' 'continua a exibição na mesma linha, mesmo com a quebra dos prints.
print(f"O resultado da divisão inteira é igual {div_int}.\nA pontencia é igual {potencia}.\nO resto é igual {resto}.")