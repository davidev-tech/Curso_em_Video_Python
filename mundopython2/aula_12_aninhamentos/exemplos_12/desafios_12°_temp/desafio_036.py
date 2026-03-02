casa = float(input("Qual o valor da casa? "))
salario = float(input("Quanto é o seu salário? "))
anos = int(input("Em quantos anos pretende pagar? "))

prestacoes = anos * 12
prestacoes_valor = casa/prestacoes
emprestimo_aprovado = salario*(30/100)

if prestacoes_valor <= emprestimo_aprovado:
    print(f"O seu emprestimo de R${casa:.2f} Reais foi APROVADO!.")
else:
    print("Seu emprestimo foi NEGADO!.")
print(f"Para pegar uma casa de R${casa:.2f} Reais em {anos} anos ", end="")
print(f"As prestações será de R${prestacoes_valor:.2f} Reais.")