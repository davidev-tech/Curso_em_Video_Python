temperatura = str(input("Qual a medida fornecida? (1) Para Celsius e (2) Para Fahrenheit: "))
if temperatura == "1":
    celsius = float(input("Qual a temperatura em Celsius? "))
    fahrenheit = celsius * 1.8 + 32
    print(f"A temperatura de {celsius:.2f}°C corresponde a {fahrenheit:.1f}°F!")
elif temperatura == "2":
    fahrenheit = float(input("Qual a temperatura em Fahrenheit? "))
    celsius = (fahrenheit-32) / 1.8
    print(f"A temperatura de {fahrenheit:.2f}°F corresponde a {celsius:.1f}°C!")
else:
    print("Informe uma opção valida!")