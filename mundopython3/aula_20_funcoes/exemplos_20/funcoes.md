Toda Função é uma rotina, ou seja, é algo que repete constantemente. As funções tem como objetivo permitir a reutilização de uma parte do código, sem que eu precise o reescrever. Além disso facilita a manuntenção do código, pois como criamos pequenos blocos no código usando funções, podemos mexer somente nele quando necessario, fazendo com que não seja necessario mexer em varias partes do código. Quando criamos uma função, estamos criando comando personalizado.
----------------------------------------------------------------------------------------------------------------------
Para definir uma função no Python, usamos a estrutura: def, ela permite a criação de uma função, seguido do nome da função, parenteses e dois ponto: def função(): 
Definimos o que queremos dentro dela, usando a indentação.

Ex:     def mostrar_linha():
            print("----------------")

Dessa forma definimos uma função.
----------------------------------------------------------------------------------------------------------------------
Caso eu queira a chamar em algum momento do código, basta eu digitar o nome seguido do parenteses: função().

Ex:

mostrar_linha()
print("           SISTEMA DE ALUNOS           ")
mostrar_linha()
mostrar_linha()
print("        CADASTRO DE FUNCIONARIOS        ")
mostrar_linha()
mostrar_linha()
print("         ERRO DO SISTEMA         ")
mostrar_linha()
----------------------------------------------------------------------------------------------------------------------
Em funções também utilizam passagem de parametros.

Ex:         def mensagem(msg):
                print(--------------------)
                print(msg)
                print(--------------------)
            

            mensagem("SISTEMAS DE ALUNOS")