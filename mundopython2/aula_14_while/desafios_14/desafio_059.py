num1 = int(input("Qual o primeiro número? "))
num2 = int(input("Qual o segundo número? "))
menu = 0
while menu != 5:
    menu = int(input("""Escolha uma opção de acordo com os números:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Respota: """))
    if menu == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} é igual {soma}.")
    elif menu == 2:
        multiplicacao = num1 * num2
        print(f"O produto entre {num1} e {num2} é igual {multiplicacao}.")
    elif menu == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f"Entre os número {num1} e {num2} o número {maior} é o maior")
    elif menu == 4:
        num1 = int(input("Qual o primeiro número? "))
        num2 = int(input("Qual o segundo número? "))
    elif menu == 5:
        print("FIM DO PROGAMA!")
    else:
        print("Opção invalida! Por favor digite uma das opções validas!")