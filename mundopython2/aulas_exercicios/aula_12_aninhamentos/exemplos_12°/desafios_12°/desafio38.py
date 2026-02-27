n1 = int(input("Qual o primeiro número? "))
n2 = int(input("Qual o segundo número? "))
if n1 > n2:
    print(f"O primeiro número {n1} é maior.")
elif n2 > n1:
    print(f"O segundo número {n2} é maior.")
else:
    print(f"Os dois números {n1} e {n2} são exatamente iguais.")