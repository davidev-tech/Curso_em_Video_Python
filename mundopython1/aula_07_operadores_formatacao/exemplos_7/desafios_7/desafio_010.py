real = float(input("Informe quantos reais você tem na carteira: R$"))
dolar = 3.27
cotacao = real / dolar
print(f"Você tem R${real:.2f}Reais e podera comprar US${cotacao:.2f}Dolares.")