peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
imc =  peso / (altura**2)

if imc < 18.5:
    print(f"Com o imc {imc:.1f} você está Abaixo do Peso.")
elif imc < 25:
    print(f"Com o imc {imc:.1f} você está no Peso Ideal.")
elif imc < 30:
    print(f"Com o imc {imc:.1f} você está com Sobrepeso")
elif imc < 40:
    print(f"Com o imc {imc:.1f} você tem Obesidade.")
else:
    print(f"Com o imc {imc:.1f} você tem Obesidade Mórbida! Cuidado!")