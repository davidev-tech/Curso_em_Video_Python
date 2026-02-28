numero = int(input("Qual o número? "))
conversoes = int(input("""Deseja convertelo para:
[ 1 ]binario
[ 2 ]octal(2)
[ 3 ]hexadecimal(3)
Resposta: """))
if conversoes == 1:
    print(f"O número {numero} em binario é igual: ",bin(numero)[2:])
elif conversoes == 2:
    print(f"O número {numero} em octal é igual: ",oct(numero)[2:])
elif conversoes == 3:
    print(f"O número {numero} em hexadecimal é igual: ",hex(numero)[2:])
else:
    print("Informe uma opção VALIDA!")