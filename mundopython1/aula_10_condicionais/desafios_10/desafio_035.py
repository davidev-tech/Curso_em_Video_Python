print("-=-" * 14)
print("Analiador de Triângulos!")
print("-=-" * 14)

reta1 = float(input("Qual o comprimento da primeira reta? "))
reta2 = float(input("Qual o comprimento da segunda reta? "))
reta3 = float(input("Qual o comprimento da terceira reta? "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("A formação de um triângulo é possivel!")
else:
    print("Não é possivel formar um triângulo")
