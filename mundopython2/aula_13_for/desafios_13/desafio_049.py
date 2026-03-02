numero = int(input("Qual o número? "))
mult = numero

for x in range(1, 11):
    resultado = mult * x 
    print(f"{x} x {mult} = {resultado}")