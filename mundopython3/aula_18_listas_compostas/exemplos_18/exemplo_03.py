lista = []
lista.append("Gustavo")
lista.append(40)
lista_2 = []
lista_2.append(lista[:]) # Quando usamos o fatiamento completo copiamos apenas o valor de lista 1 para lista 2.
lista[0] = "Hiara"
lista[1] = 18
lista_2.append(lista[:])
print(lista_2)