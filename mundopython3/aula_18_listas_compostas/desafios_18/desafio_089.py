"""
Desafio 089: Sistema de boletim escolar com armazenamento em matrizes tridimensionais.
Implementação de CRUD básico (Create e Read) com busca por indexação direta.
"""
ficha = []

while True:
    nome = str(input("Digite o nome do aluno: ")).strip()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    
    continuar_parar = " "
    while continuar_parar not in "SN":
        continuar_parar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if continuar_parar == "N":
        break

print(f"{'No.':<4}{"NOME":<10}{"MÉDIA":>8}")
print("-" * 26)
for indice, aluno in enumerate((ficha)):
  
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

print("-" * 26)
while True:
    opcao = int(input("Deseja ver a nota de qual aluno? (999 encerra o Programa): "))
    
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1:
        print(f"As notas de {ficha[opcao][0]} são {ficha[opcao][1]} ")
        print("-" * 26) 

print("FINALIZANDO...")
print(f"<<< VOLTE SEMPRE! >>>")