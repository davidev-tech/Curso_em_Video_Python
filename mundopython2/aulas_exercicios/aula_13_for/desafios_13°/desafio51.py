print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)
termo = int(input("Qual o primeiro Termo? "))
razao = int(input("Qual a Razão? "))
decimo = termo + (10 - 1) * razao
for x in range(termo, decimo + razao, razao):
    print(f"{x}",end=" ---> ")
print("ACABOU")