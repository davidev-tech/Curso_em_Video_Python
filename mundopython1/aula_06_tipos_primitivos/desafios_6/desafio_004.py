inform = input("Digite Algo: ")
print(type(inform))
print(f"{inform} contem apenas números? ",inform.isnumeric())
print(f"{inform} contem apenas letras? ", inform.isalpha())
print(f"{inform} contem apenas letras e números? ", inform.isalnum())
print(f"{inform} contem apenas letras maiúsculo? ", inform.isupper())
print(f"{inform} contem apenas letras minusculas? ", inform.islower())
print(f"{inform} contem apenas espaços? ", inform.isspace())
# O comando type verifica a tipagem da variavel.
# Os demais .is fazem a verificação de informações dos dados.
