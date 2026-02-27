faculdade = "Engenharia de Software"
print(len(faculdade))# O len analisa o comprimento da String.
print(faculdade.count('e')) # O count conta quantas vezes aquele caracter aparece.
print(faculdade.count('e', 0, 13)) # dessa forma é realizado a contagem + fatiamento.
print(faculdade.find('Soft')) # Procura qual indice começa a cadeia de caracter especificada.
print(faculdade.find('Celular')) 
# Retorna -1, pois essa String não se encontra dentro da variavel faculdade a String Celular não se encontra em nenhum ranger.
print('Software' in faculdade)
