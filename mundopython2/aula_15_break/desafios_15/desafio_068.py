from random import randint
sorteio = (1, 10)
vitorias = 0
derrotas = 0
while True:
    sorteio = randint(1, 10)
    valor_usuario = int(input("Digite um valor: "))
    while par_impar not in "PI":
        par_impar = str(input("Par ou ímpar? [P/I] ")).strip().upper()[0]
    resultado =  valor_usuario + sorteio
    if par_impar == "P":
        if resultado % 2 == 0:
           vitorias += 1
           print("-=-" * 20)
           print(f"Você jogou {valor_usuario} e o computador {sorteio}. Total de {resultado} PAR!")
           print("-=-" * 20)
           print("Você VENCEU!")
           print("Vamos jogar novamente...")
        else:
            derrotas += 1
            print("-=-" * 20)
            print(f"Você jogou {valor_usuario} e o computador {sorteio}. Total de {resultado} ÍMPAR!")
            print("-=-" * 20)
            print("Você PERDEU!")
            break
    elif par_impar == "I":
        if resultado % 2 != 0:
           vitorias += 1
           print("-=-" * 20)
           print(f"Você jogou {valor_usuario} e o computador {sorteio}. Total de {resultado} ÍMPAR!")
           print("-=-" * 20)
           print("Você VENCEU!")
           print("Vamos jogar novamente...")
        else:
            derrotas += 1
            print("-=-" * 20)
            print(f"Você jogou {valor_usuario} e o computador {sorteio}. Total de {resultado} PAR!")
            print("-=-" * 20)
            print("Você PERDEU!")
            break
    else:
        print("Opção INVALIDA! Digite: [P/I] ")
if vitorias == 0:
    print("GAME OVER! Você não venceu nenhuma vez.")
elif vitorias == 1:
    print(f"GAME OVER! Você venceu {vitorias} vez.")
else:
    print(f"GAME OVER! Você venceu {vitorias} vezes.")