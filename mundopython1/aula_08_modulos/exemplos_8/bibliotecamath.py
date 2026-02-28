#import math
#num = int(input("Informe um número: "))
#raiz = math.sqrt(num)
# Na linha 3 definimos o modulo math, a função de raiz .sqrt, e da onde vira o valor para a variavel raiz (num)
#print(f"A raiz de {num} é igual {raiz:.2f}")

from math import sqrt, floor
num = int(input("Informe um número: "))
raiz = sqrt(num)
print(f"A raiz de {num} é igual {floor(raiz)}")