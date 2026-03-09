"""
Desafio 086: Manipulação de listas bidimensionais através de loops aninhados para controle de índices.
"""
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
somatorio = 0

for indice in range(0,3):
    for contador in range(0,3):
        matriz[indice][contador] = int(input("Digite um valor: "))

for indice in range(0,3):
    for contador in range(0,3):
        print(f"{matriz[indice][contador]:^5}",  end="")
    print()