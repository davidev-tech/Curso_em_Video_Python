frase = str.upper(input("Qual a frase? ")).strip()
print(f"A letra A aparece: {frase.count('A')} vezes.")
print(f"A primeira aparição da letra A é no indice: {frase.find('A') + 1}")
print(f"A ultima vez que a letra A aparece é no indice: {frase.rfind('A') + 1}")