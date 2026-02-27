cateto_adjacente = float(input("Informe o comprimento do cateto adjacente: "))
cateto_oposto = float(input("Informe o comprimento do Cateto Oposto: "))
# hipotenusa = ((cateto_adjacente**2 + cateto_oposto**2)**(1/2))
# print(f"A Hipotenusa desse triângulo retângulo é igual {hipotenusa} ")

from math import hypot
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f"A Hipotenusa desse triângulo retângulo é igual {hipotenusa:.2f} ")