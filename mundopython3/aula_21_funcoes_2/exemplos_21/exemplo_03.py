def contador(i,f,p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: inicia a contagem.
    :param f: Marca o fim da contagem.                
    :param p: Pontua a quantidade do salto.
    return: Sem retorno.
    """    #<-- A DOCSTRING  da função contador
    c = i
    while c <= f:
        print(f"{c}", end=' ')
        c += 1
    print("FIM!")


help(contador)