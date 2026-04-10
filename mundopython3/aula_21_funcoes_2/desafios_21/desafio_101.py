def calcular_idade(ano_nasc):
    """
    Calcula a idade baseada no ano atual.
    :param ano_nasc: O ano de nascimento do usuário.
    :return: A idade calculada (int).
    """
    from datetime import date

    data_atual = date.today().year
    idade = data_atual - ano_nasc

    return idade


def verificar_status_voto(idade_eleitor):
    """Verifica a obrigatoriedade do voto com base na idade."""

    if 18 <= idade_eleitor < 70:
        return f'Com {idade_eleitor} anos: VOTO OBRIGATÓRIO!'
    elif idade_eleitor < 16:
        return f'Com {idade_eleitor} anos: VOCÊ NÃO VOTA!'
    else:
        return f'Com {idade_eleitor} anos: VOTO OPCIONAL!'


print("--" * 12)
ano_nascimento = int(input("Em que ano você nasceu? "))
idade = calcular_idade(ano_nascimento)
print(verificar_status_voto(idade))
