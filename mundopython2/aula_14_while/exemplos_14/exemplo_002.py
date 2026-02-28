'''num = 1
while num != 0:
    num = int(input("Digite um valor: "))
print("Fim")'''

resp = "S"
while resp == "S":
    num = int(input("Digite um número: "))
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()    