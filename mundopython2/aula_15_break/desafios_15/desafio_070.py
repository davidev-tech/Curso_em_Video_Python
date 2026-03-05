total_gasto = 0
produtos_mil_mais = 0
nome_produto_mais_barato = " "
valor_produto_mais_barato = 0
parar_continuar = " "

print("-" * 30)
print("       LOJA TEC INOVA       ")
print("-" * 30)

while True:
    parar_continuar = " "
    produto_nome = " "
    produto_valor = -1
    produto_nome = str(input("Qual o nome do produto? ")).strip().upper()

    while produto_valor < 0:
        produto_valor = float(input("Qual o valor do produto? R$"))
    total_gasto += produto_valor
    
    if nome_produto_mais_barato == " ":
        nome_produto_mais_barato = produto_nome
    if valor_produto_mais_barato == 0:
        valor_produto_mais_barato = produto_valor
    if produto_valor > 1000:
        produtos_mil_mais += 1
    if produto_valor < valor_produto_mais_barato:
        valor_produto_mais_barato = produto_valor
        nome_produto_mais_barato = produto_nome

    while parar_continuar not in "SN":
        parar_continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
        
    if parar_continuar == "N":
        break
    
print("-" * 12,"FIM DO PROGRAMA","-" * 12)
print(f"O total gasto na compra foi de R${total_gasto:.2f} Reais.")
print(f"{produtos_mil_mais} Produtos custam mais de R$1000 reais.")
print(f"O produto mais barato foi {nome_produto_mais_barato} custando R${valor_produto_mais_barato:.2f} Reais.")