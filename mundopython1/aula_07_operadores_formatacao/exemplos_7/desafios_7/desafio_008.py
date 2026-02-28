valor = float(input("Informe um valor em metros: "))
dm = valor * 10
centimetros = valor * 100
milimetros = valor * 1000
dam = valor / 10
hm = valor / 100
km = valor / 1000

print(f"{valor}m em decimetro é igual {dm}dm\nEm centímetros é igual {centimetros}cm.\nEm milímetros é igual {milimetros}mm.")
print(f"Em decâmetros é igual {dam}dam.\nEm hectômetros é igual {hm}hm.\nEm quilômetros é igual {km}km.")