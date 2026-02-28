dias_alugados = int(input("Quantos dias alugados? "))
kms_rodados = float(input("Quantos kms rodados? "))
dias_preco = 60*dias_alugados
kms_preco = 0.15*kms_rodados
preco_pago = (dias_preco+kms_preco)
print(f"O total a pagar é de R${preco_pago:.2f}Reais.")