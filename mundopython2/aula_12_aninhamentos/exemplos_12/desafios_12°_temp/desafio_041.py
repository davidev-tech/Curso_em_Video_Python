from datetime import date
ano_atual = date.today().year
nascimento = int(input("Em que ano o atleta nasceu? "))
idade = ano_atual - nascimento

if idade <= 9:
    print(f"O atleta nasceu em {nascimento}. E com {idade} anos faz parte da categoria: MIRIM!")
elif idade <= 14:
    print(f"O atleta nasceu em {nascimento}. E com {idade} anos faz parte da categoria: INFANTIL!")
elif idade <= 19:
    print(f"O atleta nasceu em {nascimento}. E com {idade} anos faz parte da categoria: JUNIOR!")
elif idade <= 25:
    print(f"O atleta nasceu em {nascimento}. E com {idade} anos faz parte da categoria: SENIOR")
else:
    print(f"O atleta nasceu em {nascimento}. E com {idade} anos faz parte da categoria: MASTER!")