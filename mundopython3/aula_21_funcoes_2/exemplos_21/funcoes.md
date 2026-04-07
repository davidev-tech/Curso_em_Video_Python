INTERACTIVE HELP: Para usar a ajuda interativa, basta usar a função help(), abrindo o INTERACTIVE HELP no terminal, digitamos o comando que temos duvidas e ele irá mostrar a documentação daquele comando. Para sair basta usar o comando: "q", "quit" ou "exit".
Também podemos usar help(comando) no código para ser mais direto. O help() é uma função formatada para humanos (bonitinha e organizada).

Ex:     help(print)
----------------------------------------------------------------------------------------------------------------------------------
Uma segunda forma é o uso do __doc__: Para utilizar usamos print(comando.__doc__) Assim temos usa segunda forma de acessar a documentação daquele comando. O .__doc__ é o atributo "crú" (string pura).

Ex:     print(len.__doc__)
----------------------------------------------------------------------------------------------------------------------------------
DOCSTRINGS: São documentações feita pelo desenvolvedor sobre a sua função, ficando logo a baixo da linha de definição da função. Oobjetivo delas é ser uma especie de manual para outros programadores ou até mesmo usuários.

Ex:        
        def contador(i,f,p):
            """
            --> Faz uma contagem e mostra na tela.
            :param i: inicia a contagem.
            :param f: Marca o fim da contagem.                
            :param p: Pontua a quantidade do salto.
            return: Sem retorno.
            """  


Para ler a sua própria Docstring enquanto programa, basta digitar help(sua_funcao) no console. O Python vai buscar exatamente o que você escreveu entre as aspas triplas """.
----------------------------------------------------------------------------------------------------------------------------------
Default Parameters é um metodo utilizando um default para evitar que a função der um erro requerendo um argumento para um determinado parametro que não recebeu um argumento. Basicamente quando definimos 0 como argumento para os parametros na função a baixo, ele já tem aquele valor tornando a requisição de um argumento opcinal, pois usamos o 0 como argumento padrão. Parametros obrigatorios veem antes dos parametros opcionais.

Ex:         def somar(a=0, b=0, c=0):
                s = a + b + c
                print(f"A soma vale {s}")


            somar(3, 2, 5)
            somar(5, 2)
            somar(2)
            somar()
----------------------------------------------------------------------------------------------------------------------------------
Escopo de Variaveis: O Escopo de declarações é o local onde a variavel vai ou não vai existir, ou seja, uma variavel pode existir apenas dentro de uma função, sendo uma variavel local, ou no programa principal, sendo uma variavel global. Para modificar uma variavel global de dentro de uma função usamos o comando: global variavel. Dessa forma acessamos o endereço da variavel global na memoria, tornando possivel modificar variaveis globais de dentro da uma função.
----------------------------------------------------------------------------------------------------------------------------------
Retornando valores: Usamos o comando return variavel para retorna um valor da variavel de dentro da função para o programa principal, permitindo que o valor seja exibido diretamente ou que o valor seja atribuido a uma variavel do programa principal, dessa forma o valor deixa de ser de uma variavel local e passa a ser de uma variavel global. Obs: assim que usamos o return em uma função, nada a baixo será lido, pois a função encerra ali.