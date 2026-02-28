altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))
balde = 2
area = ((altura * largura))
litros_tinta = (area / balde)
print(f"A sua parede tem a dimensão de {altura}x{largura} e sua aréa é de {area}m²")
print(f"Para pintar essa parede, você precisará de {litros_tinta}L de tinta.")