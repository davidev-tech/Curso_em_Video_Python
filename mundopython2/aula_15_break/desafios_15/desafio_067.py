numero = 0
contador = 1
produto = 0
while True:
    numero = int(input("Deseja ver a tabuada de qual valor? "))
    if numero < 0:
        break
    print("-" * 35)  
    for contador in range(1, 11):
        produto = numero * contador     
        print(f"{numero} x {contador} = {produto}")
    print("-" * 35)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")