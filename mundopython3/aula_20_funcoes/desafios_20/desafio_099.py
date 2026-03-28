from time import sleep


def exibir_maior(*valores):
    '''Exibindo valores na tela e buscando o maior valor passado'''  
    maior = 0
    contador = 0
    print("Analisando valores passados...")
    for valor in valores:
        print(f"{valor}", end=' ', flush=True)
        sleep(0.5)
    
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor 
        contador += 1

    print(f"Foram informados {len(valores)} valores ao todo.")
    print(f"O maior valor informado foi: {maior}") 
    print("-=" * 20)


print("-=" * 20)
exibir_maior(2, 4, 6, 9, 7)
exibir_maior(1, 4)
exibir_maior(4)
exibir_maior(3, 5, 6)