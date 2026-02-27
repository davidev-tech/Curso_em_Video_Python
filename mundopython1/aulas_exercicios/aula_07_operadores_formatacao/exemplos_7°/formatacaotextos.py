nome = input("Qual o seu nome? ")
print(f"Prazer {nome:20}!")   # imprimi o texto e avança 20 espaços a frante, antes da proxima string.
print(f"Prazer {nome:>20}!")  # Alinha o nome a direita, após 20 espaços em branco. 
print(f"Prazer {nome:<20}!")  # Alinha o nome a esquerda, e pular 20 espaços.
print(f"Prazer {nome:^20}!")  # Centraliza o texto.

print(f"Prazer {nome:=^20}!") # Centraliza o texto e preenche os espaços em branco com o sinal desejado.
print(f"Prazer {nome:-^20}!")
print(f"Prazer {nome:+^20}!")