from time import sleep


def exibir_contagem(inicio, fim, salto):
    '''Exibindo Progressão Aritmédica'''
    if salto <= 0:
        salto = 1
    if inicio < fim:
        for contador in range(inicio, fim + 1, salto):
            print(f"{contador}", end=" ", flush=True)
            sleep(1)
    else:
        for contador in range(inicio, fim - 1, - salto):
            print(f"{contador}", end=" ", flush=True)
            sleep(1)
    print("FIM!")
    print("-=" * 20)


print("-=" * 20)
print("Contagem de 1 a 10 de 1 em 1.")
exibir_contagem(1, 10, 1)
print("Contagem de 10 a 0 de 2 em 2.")
exibir_contagem(10, 0, 2)
contagem = []
print("Agora é a sua vez de personalizar a contagem: ")
contagem.append(int(input("Qual número marcara o inicio da contagem? ")))
contagem.append(int(input("Qual número marcara o fim da contagem? ")))
contagem.append(int(input("Qual o tamanhos do salto? ")))
print("-=" * 20)
print(f"Contagem de {contagem[0]} até {contagem[1]} de {contagem[2]} em {contagem[2]}")
exibir_contagem(*contagem)