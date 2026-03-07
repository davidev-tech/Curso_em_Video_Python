lista = []
lista.append("Gustavo")
lista.append(40)
lista_2 = []
lista_2.append(lista) # Ligação indireta.
lista[0] = "Hiara"
lista[1] = 18
lista_2.append(lista)
print(lista_2)