from time import sleep
print("-=-" * 20)
velocidade = float(input("A quantos km/h o cidadão estava? "))
print("-=-" * 20)
print("PROCESSANDO...")
sleep(3)
if velocidade > 80:
    multa = ((velocidade - 80) * 7 )
    print(f"A multa do cidadão será de: R${multa:.2f} Reais!")
else:
    print("O cidadão está dentro do limite de velocidade!")
    print("Tenha um bom dia! Dirija com segurança!")