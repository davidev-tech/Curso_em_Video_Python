distancia = float(input("Qual a distancia da viagem em km/h: "))
if distancia <= 200:
    custo_km = 0.5
    passagem = distancia * custo_km 
else:
    custo_km = 0.45
    passagem = distancia * custo_km
print(f"O custo da viajem de {distancia:.2f}km ficou R${passagem:.2f} Reais.")