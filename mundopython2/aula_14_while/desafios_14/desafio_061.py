termo = int(input("Qual o Termo? "))
razao = int(input("Qua a Razão? "))
termo_atual = termo 
contador = 1

while contador <= 10:
    print(f"{termo_atual}", end=" --> ")
    contador += 1
    termo_atual += razao
    
print("FIM") 