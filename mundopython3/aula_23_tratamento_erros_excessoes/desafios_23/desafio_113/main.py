from tratamento_dados import tratar_numero_inteiro, tratar_numero_real


# =============================================================================================
# DESAFIO 113: Validando entradas do usuário.
# Objetivo: Criar o maximo de segurança em relação a tipagem do dado. 
# Conceitos: Tratamento de dados usando loops, tratamento de exceções e modularização.
# =============================================================================================

numero_inteiro = tratar_numero_inteiro()
numero_real = tratar_numero_real()
print(f'\033[0;35mO número inteiro informado foi: {numero_inteiro} e real: {numero_real}\033[m')