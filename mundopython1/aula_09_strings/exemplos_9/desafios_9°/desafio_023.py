numero = int(input("Digite o número de 0 a 9999: "))
unidade_milhar = numero // 1000 % 10
centenas = numero // 100 % 10
dezenas = numero // 10 % 10
unidade = numero // 1 % 10
print(f"Esse númerto possui: {unidade_milhar} Unidades de Milhar.")
print(f"Esse número possui: {centenas} Centenas.")
print(f"Esse número possui: {dezenas} Dezenas.")
print(f"Esse número possui: {unidade} Unidades")

