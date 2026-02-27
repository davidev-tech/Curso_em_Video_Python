reta1 = float(input("Qual o comprimento do primeiro segmento? "))
reta2 = float(input("Qual o comprimento do segundo segmento? "))
reta3 = float(input("Qual o comprimento do terceiro segmento? "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print("Esse triângulo é Equilátero! Todos os lados são iguais.")
    elif reta1 != reta2 != reta3:
         print("Esse triângulo é Escaleno! Todos os lados são diferentes.")
    else:
        print("Esse triângulo é Isóceles! Somente 1 lado é diferente.")
else:
    print("Com esses comprimentos de retas não é possivel formar um triângulo.")
