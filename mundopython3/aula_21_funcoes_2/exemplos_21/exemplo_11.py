def verificar_par_ou_impar(num=0):
    if num % 2 == 0:
        return f"{num} é PAR!"
    else:
        return f"{num} é IMPAR!"
    

numero = int(input("Digite um número para descobrir se é par ou impar: "))
resp = str(input(verificar_par_ou_impar(numero)))
print(resp)