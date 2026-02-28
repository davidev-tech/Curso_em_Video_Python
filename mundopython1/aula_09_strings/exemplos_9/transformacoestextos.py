materia_escolar = 'Curso de Matemática'
print(materia_escolar)
nova_materia_escolar = materia_escolar.replace('Matemática', 'História')
# O replece cria uma copia da String na memoria com a mudança sugerida, sem afetar a String principal.
print(nova_materia_escolar)
print(materia_escolar.upper()) # Deixa tudo em maisculo.
print(materia_escolar.lower()) # Deixa tudo em minusculo.
print(materia_escolar.capitalize()) # Deixa somente o primeiro caracter em maisculo e o resto minusculo.
print(materia_escolar.title())
# Faz com que a inicial de cada palavra fique em maisculo, ele faz a distinção de palavaras por meio dos espaços.

frase = '   Aprendendo Pyton  '
print(frase)
frase = frase.strip() # Remove os espaços desnecessarios do inicio e final da String.
# rstrip() remove os espaços apenas da direita e o lstrip() apenas da esquerda.
print(frase)
materia_escolar = materia_escolar.split() # Reconhece os espaços e divide a String em Strings, criando uma lista com Strings.
print(materia_escolar [2] [3]) # Ele pega o terceiro item da lista e depois exibi a terceira letra do item.
print(' '.join(materia_escolar)) # O ''.join() Faz o oposto do .split() e junta tudo.