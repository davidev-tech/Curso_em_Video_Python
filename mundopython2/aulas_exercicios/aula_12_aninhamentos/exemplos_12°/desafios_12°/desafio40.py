nota1 = float(input("Qual foi a primeira nota: "))
nota2 = float(input("Qual foi a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2} a media do aluno é {media:.1f}.")
if media < 5:
    print("O aluno está REPROVADO!")
elif media < 7:
    print("O aluno está de RECUPERAÇÃO!")
else:
    print("O aluno está APROVADO!")