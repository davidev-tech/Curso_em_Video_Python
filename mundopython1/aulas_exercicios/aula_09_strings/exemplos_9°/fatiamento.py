faculdade = ("Engenharia de Software")
print(faculdade)
print(faculdade[7])
print(faculdade[14:21])
print(faculdade[14:22:2])
print(faculdade[:10])# quando omitimos o indice de inicialização o programa começa a contagem do indice 0.
print(faculdade[14:])# quando omitimos o indice de encerramento o programa realiza a contagem até o final.
print(faculdade[::])
print(faculdade[14::3]) # Vai de 14 até o final saltando de 3 em 3.
#Aqui temos dois exemplos, no primeiro a cadeia de caracter é toda exibida.
#Ja no segundo exemplo é feito o uso da tecnica de fatiamento para mostrar apenas um caracter que é especificado pelo seu indice.
#Já no terceiro exemplo ele pega do indice 14 até o 20, a contagem é até o penultimo indice.
# No quanto exemplo ele pega do ranger de 14 a 22, no entanto saltando de 2 em 2.
