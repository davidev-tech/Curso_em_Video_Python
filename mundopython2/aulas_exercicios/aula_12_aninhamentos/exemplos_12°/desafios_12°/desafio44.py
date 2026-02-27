produto = float(input("Qual o preço do produto? "))
forma_pagamento = int(input("""Qual a forma de Pagamento?
[ 1 ] Dinheiro.
[ 2 ] Cheque.
[ 3 ] Cartão.
Resposta:                            
"""))
if forma_pagamento == 1 or forma_pagamento == 2:
    desconto = produto * (10/100) 
    produto_desconto = produto - desconto
    print(f"O produto de R${produto} Reais. à vista recebe um desconto de: 10%.")
    print(f"O produto sairá por R${produto_desconto:.2f} Reais.")
elif forma_pagamento == 3:
    parcelado_naoParcelado = int(input("""À vista ou Parcelado?
[ 1 ] À vista
[ 2 ] Parcelado
Resposta:
"""))
    if parcelado_naoParcelado == 1:
        desconto = produto * (5/100)
        produto_desconto = produto - desconto
        print(f"O produto de R${produto} Reais com um desconto de: 5%.")
        print(f"O produto sairá por R${produto_desconto:.2f} Reais.")
    elif parcelado_naoParcelado == 2:
        parcelas = int(input("Em quantas vezes irá parcelar? "))
        if parcelas == 2:
            print(f"O cliente não terá desconto. O valor a ser pago permanecerá R${produto} Reais.")
        elif parcelas <= 12:
            juros = produto * (20/100)
            valor_juros = produto + juros
            print(f"O valor do produto erá R${produto} Reais.")
            print(f"Porém com {parcelas} parcelas temos um juros de 20%.")
            print(f"O valor do produto passa a ser R${valor_juros:.2f} Reais.")
            print(f"O cliente execedeu o valor maximo de 12 Parcelas.")
    else:
        print("Opção invalida! Por favor, recomece o procedimento.")
else:
        print("Opção invalida! Por favor, recomece o procedimento.")