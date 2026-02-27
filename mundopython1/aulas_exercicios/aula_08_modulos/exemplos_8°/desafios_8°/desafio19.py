from random import choice
aluno1 = str(input("Qual o nome do primeiro aluno? "))
aluno2 = str(input("Qual o nome do segundo aluno? "))
aluno3 = str(input("Qual o nome do terceiro aluno? "))
aluno4 = str(input("Qual o nome do quarto aluno? "))
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(alunos)
print(f"O aluno que foi sorteado para apagar o quadro foi {sorteio}.")