"Exibindo o número que o usuário digitar de 0 a 20 por extenso"

numeros1 = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ")
numeros2 = ("ONZE", "DOZE", "TREZE", "CATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
numeros = numeros1 + numeros2

while True:
    numero_usuario = -1
    continuar_parar = " "
    
    while numero_usuario < 0 or numero_usuario > 20:
        numero_usuario = int(input("Digite um número de 0 a 20: "))
    print(f"O número {numero_usuario} por extenso é {numeros[numero_usuario ]}") 

    while continuar_parar not in "SN":
        continuar_parar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if continuar_parar == "N":
        break