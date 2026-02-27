frase = str(input("Digite uma Frase ou Palavra para saber se ela é um políndromo: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
# inverso = junto[::-1]

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f"A frase {junto} é um políndromo.")
else:
    print(f"A frase {junto} não é um políndromo.")
print(f"O inverso de {junto} é {inverso}.")