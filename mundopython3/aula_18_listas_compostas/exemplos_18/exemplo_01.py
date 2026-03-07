lista = []
lista.append("Gustavo")
lista.append(40)
lista_2 = lista # Foi formado um elo entre os dois endereços. Ligação direta.
lista[1] = "Hiara"
lista[0] = 18
print(lista_2)
# Ambas as listas estão apontando para o mesmo local na memoria.