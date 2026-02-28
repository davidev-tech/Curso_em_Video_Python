num = int(input("Qual o número? "))
fatorial = num
contadora = num - 1
while contadora > 0:
    fatorial = fatorial * contadora
    contadora = contadora - 1
print(f"O valor fatorial de {num} é {fatorial}.")