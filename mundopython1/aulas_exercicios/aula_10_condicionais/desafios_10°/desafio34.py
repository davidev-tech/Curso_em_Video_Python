salario = float(input("Quanto é o salário do funcionario? "))
if salario > 1250:
    aumento = (salario * (10/100))
else:
    aumento = (salario * (15/100))
novo_salario = salario + aumento
print(f"O funcionario ganhava R${salario:.2f} Reais.")
print(f"Recebeu um aumento de R${aumento:.2f} Reais.")
print(f"O seu novo salario passa a ser R${novo_salario:.2f} Reais.")