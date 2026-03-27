def exibir_texto(txt):
    '''Exibindo bordas dinamicas.'''
    tamanho_texto = len(txt)
    bordas = tamanho_texto + 4
    print("~" * bordas)
    print(f"{txt:^{bordas}}")
    print("~" * bordas)


texto = str(input("Digite um texto? ")).strip()
exibir_texto(texto)