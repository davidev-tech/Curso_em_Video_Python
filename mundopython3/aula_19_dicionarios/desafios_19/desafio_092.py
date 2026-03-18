"""
Desafio 092: Cadastro de Trabalhador e Cálculo de Aposentadoria.
Uso da biblioteca datetime para manipulação de anos correntes e aplicação de 
lógica de negócio condicional (CTPS) em estruturas de dicionários.
"""
from datetime import datetime
ficha_usuario = {}
ano_atual = datetime.now().year

ficha_usuario['nome'] = str(input("Digite o nome do usuário: ")).strip()
ficha_usuario['ano_nascimento'] = int(input("Digite o ano de nascimento do usuário: "))
ficha_usuario['idade'] = ano_atual - ficha_usuario["ano_nascimento"]
ficha_usuario['CTPS'] = int(input("Carteira de Trabalho (0 não tem): "))

if ficha_usuario['CTPS'] != 0:
    ficha_usuario['ano_contratação'] = int(input("Qual o ano de contratação do usuário? "))
    ficha_usuario['salario'] = float(input("Qual o salario do usuário? R$"))
    ficha_usuario['ano_aposentadoria'] = ficha_usuario['ano_contratação'] - ficha_usuario['ano_nascimento'] + 35

del ficha_usuario['ano_nascimento']

print("-=" * 35)
for k, v in ficha_usuario.items():
    if k == 'salario':
        print(f" - {k} é igual a {v:.2f}")
    else:
        print(f" - {k} é igual a {v}")