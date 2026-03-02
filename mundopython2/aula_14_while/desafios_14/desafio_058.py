from random import randint
sorteio = randint(1,10)
palpites = 1
usuario = int(input("""Pensei em um número de 1 a 10. Qual número eu pensei?
Resposta: """))

while usuario != sorteio:
    if usuario < sorteio:
        print("O número que eu pensei é maior.")
    else:
        print("O número que eu pensei é menor.")
    usuario = int(input("""Qual número eu pensei?
Resposta: """))
    palpites += 1
    
print(f"Parábens! Você acertou! A resposta realmente era: {sorteio}")
print(f"Foram nescessarios {palpites} palpites para você acertar.")