from random import randint
from time import sleep
numero = randint(1,5)
sorteio = numero
print("-=-" * 20)
print("Vou pensar em um número de 1 a 5. Tente adivinhar...")
print("-=-" * 20)
resposta = int(input("Adivinhe o número que estou pensando de 1 a 5: "))
print("PROCESSANDO...")
sleep(3)
if resposta == sorteio:
    print("Parabéns! você acertou!")
else:
    print("Desculpa! Você errou! ")
    print(f"A resposta era: {sorteio} e não {resposta}.")