numero = int(input("Qual o número: "))
quantidade_divisores = 0
for x in range(1,numero + 1):
    divisor = x
    if numero % divisor == 0:
        quantidade_divisores += 1
if quantidade_divisores == 2:
        print(f"O número {numero} foi divisivel {quantidade_divisores} vezes.")
        print(f"O número {numero} é primo!")     
else:
        print(f"O número {numero} foi divisivel apenas {quantidade_divisores} vezes.")
        print(f"O número {numero} não é primo!") 