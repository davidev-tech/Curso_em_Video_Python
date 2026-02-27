produto = float(input("Informe o valor do produto: "))
pagamento = input("Qual a forma de pagamento? Digite(1) Para a vísta e (2) para parcelado: ")
if pagamento == "1":
    porcentagem_desconto = 5/100
    valor_desconto = (produto*porcentagem_desconto)
    novo_preco_desconto = (produto - valor_desconto)
    print(f"O valor do produto era: R${produto:.2F} Reais\nCom o desconto de: {porcentagem_desconto}%\nO preço a ser pago no produto será de: R${novo_preco_desconto:.2F} Reais.")
elif pagamento == "2":
    porcentagem_aumento = 7/100
    valor_aumento = (produto*porcentagem_aumento)
    novo_preco_aumento = (produto + valor_aumento)
    print(f"O valor do produto era: R${produto:.2f} Reais\nCom o aumento de: {porcentagem_aumento}% da parcela\nO preço a ser pago no produto será de: R${novo_preco_aumento:.2f} Reais.")
else:
    print("Informe uma opção valida!")