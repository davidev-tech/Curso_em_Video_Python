"""
Desafio 087: Análise de dados em matriz 3x3 (Soma de pares, colunas e valores máximos).
"""
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatorio_pares = 0
somatorio_terceira_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um número para {linha} {coluna}: "))

print("-=-" * 20)    
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"{matriz[linha][coluna]:^5}", end="")
    print()
print("-=-" * 20)

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somatorio_pares += matriz[linha][coluna] 

        if coluna == 2:
            somatorio_terceira_coluna += matriz[linha][coluna] 
     
        if linha == 1:
            if coluna == 0:
                maior_valor_segunda_linha = matriz[linha][coluna] 
            else:
                if matriz[linha][coluna] > maior_valor_segunda_linha:
                    maior_valor_segunda_linha = matriz[linha][coluna] 

print(f"A soma de todos os valores pares digitado é: {somatorio_pares}.")
print(f"A soma dos valores da terceira coluna é: {somatorio_terceira_coluna}.")
print(f"O maior valor da segunda linha é: {maior_valor_segunda_linha}")