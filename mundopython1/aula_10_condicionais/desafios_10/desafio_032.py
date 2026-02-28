from datetime import date
ano = int(input("Qual ano devo analisar? Coloque 0 para analisar o ano atual: "))
ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0: 
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")