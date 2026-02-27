from math import radians, sin, cos, tan
grau = int(input("Informe o Ângulo: "))
radiano = radians(grau)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print(f"O seno de {grau} é igual: {seno:.2f}\nO cosseno é igual: {cosseno:.2f}\nA tangente é igual: {tangente:.2f}")