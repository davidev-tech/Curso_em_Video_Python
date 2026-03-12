"""
Desafio 086: Manipulação de listas bidimensionais através de loops aninhados para controle de índices.
"""
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
somatorio = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valo para {linha}, {coluna}: "))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"{matriz[linha][coluna]:^5}",  end="")
    print() # Só para quebrar a linha antes de voltar para o loop principal