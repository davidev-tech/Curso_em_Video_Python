lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

for comida in (lanche):
    print(f"Eu vou comer {comida}.") # Te devolve apenas o item.

for contador in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[contador]}. Na posição {contador}")
# Caso queira ver apenas o indice basta tirar o lanche.

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida}. Na posição {pos}.")
print("Comi demais.")
# Duas formas diferentes de fazer a mesma coisa.