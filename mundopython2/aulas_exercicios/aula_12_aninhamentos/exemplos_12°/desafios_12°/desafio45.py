from random import choice
from time import sleep
jokempo = ("Pedra","Papel","Tesoura")
sorteio = choice(jokempo)
opcao_usuario = int(input("""Escolha uma opção: 
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura                                                      
Resposta:  """))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
if opcao_usuario != 1 and opcao_usuario != 2 and opcao_usuario != 3:
    print("As opções validas são 1, 2 e 3. Recomece o Processo.")
else:
    if sorteio == "Pedra":
        if opcao_usuario ==  1:
            print(f"EMPATAMOS! Tambêm escolhi {sorteio}.")
        elif opcao_usuario == 2:
            print(f"Você GANHOU! Eu escolhi {sorteio} e Papel ganha de {sorteio}.")
        else:
            print(f"Eu GANHEI! Escolhi {sorteio} e {sorteio} ganha de Tesoura.")
    elif sorteio == "Papel":
        if opcao_usuario ==  1:
            print(f"Eu GANHEI! Escolhi {sorteio} e {sorteio} ganha de Pedra.")      
        elif opcao_usuario == 2:
            print(f"EMPATAMOS! Tambêm escolhi {sorteio}.")
        else:
            print(f"Você GANHOU! Eu escolhi {sorteio} e Tesoura ganha de {sorteio}.")
    elif sorteio == "Tesoura":
        if opcao_usuario ==  1:
            print(f"Você GANHOU! Eu escolhi {sorteio} e Pedra ganha de {sorteio}.")       
        elif opcao_usuario == 2:
            print(f"Eu GANHEI! Escolhi {sorteio} e {sorteio} ganha de Papel.")      
        else:
            print(f"EMPATAMOS! Tambêm escolhi {sorteio}.")
    print("FIM DE JOGO!")