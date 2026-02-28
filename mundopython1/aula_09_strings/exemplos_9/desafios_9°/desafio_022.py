nome = str(input("Qual o nome completo da pessoa? ")).strip()
print("Analisando seu nome...")
print(f"O nome com todas as letras em maisculo: {nome.upper()}")
print(f"O nome com todas as letras em minusculo: {nome.lower()}")
print(f"Quantas letras o nome tem: {len(nome.replace(' ', ''))} Letras.") # Não esta contando os espaços.
print(f"Quantas letras o primeiro nome tem: {len(nome.split()[0])} Letras.")