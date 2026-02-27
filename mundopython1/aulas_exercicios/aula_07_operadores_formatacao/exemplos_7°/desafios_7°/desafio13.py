salario = float(input("Informe o salário do funcionario: R$"))
aumento = 15/100
valor_aumento = salario*aumento
novo_salario = salario + valor_aumento

print(f"O valor salarial do funcionario era de: R${salario} Reais\nCom um aumento de: {aumento}%\nO salario passou a ser R${novo_salario:.2f} Reais,",end= " ")
print(f"O funcionario recebeu um aumento de R${valor_aumento:.2f} Reais.")