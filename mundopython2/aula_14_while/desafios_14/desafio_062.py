'''termo = int(input("Qual o Termo? ")) # Minha primeira versão.
razao = int(input("Qua a Razão? "))
termo_atual = termo 
contador = 1
resposta = 1
numero_imprimidos = 0

while contador <= 10:
    print(f"{termo_atual}", end=" ")
    numero_imprimidos += 1
    contador += 1
    termo_atual += razao
while resposta != 0:
    resposta = int(input("""Deseja saber mais alguns termos da PA? ou Parar?
[ ? ] +TERMOS PA
[ 0 ] PARAR
Resposta:  """))
    if resposta != 0:
        contador = 1
        while contador <= resposta:   
             print(f"{termo_atual}", end=" ")
             numero_imprimidos += 1
             termo_atual += razao       
             contador += 1  
print("FIM DA CONTAGEM!") 
print(f"{numero_imprimidos} números foram imprimidos.")'''

termo = int(input("Qual o termo? "))  # Versão otimizada.
razao = int(input("Qual a razão? "))
termo_atual = termo
contador = 0
total = 0
mais = 10

while mais != 0:
    total += mais 
    while contador < total:
        print(f"{termo_atual}", end=" --> ")
        termo_atual += razao
        contador+= 1
    print("Pausa")
    mais = int(input(f"""Digite a quantidade de termos que deseja ver a mais.
Caso deseje parar pressione [0].
Resposta: """))
    
print(f"{total} foram imprimidos.")

