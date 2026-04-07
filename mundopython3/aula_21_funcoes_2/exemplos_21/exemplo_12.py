def verificar_par_ou_impar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
    

numero = int(input("Digite um número para descobrir se é par ou impar: "))
if verificar_par_ou_impar(numero):
    print(f"{numero} é PAR!")
else:
    print(f"{numero} é IMPAR!")