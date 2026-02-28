valor_saque = int(input("Qual o valor do saque? R$"))
total = valor_saque
total_cedulas = 0
cedula = 50
print("=" * 20)
print("     BANCO DO INTEC     ")
print("=" * 20)
while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"{total_cedulas} foram de cedulas de R${cedula} Reais")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula =1
        total_cedulas = 0
        if total == 0:
            break
print("=" * 20)
print("Volte sempre ao BANCO INTEC! Tenha um bom dia!")