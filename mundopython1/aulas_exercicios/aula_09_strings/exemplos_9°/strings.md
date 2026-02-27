Uma cadeia de caracter é a mesma coisa que uma String.
Ex: "Engenharia de Software"
Toda cadeia de texto no Python está entre aspas simples ('texto') ou aspas duplas ("texto").
----------------------------------------------------------------------------------------------------------------------------------
faculdade = Engenharia de Software
O computador não salva a String inteira em uma memoria, mas cria micro espaços dentro da memoria e guarda cada caracter em um espaço diferente.
Ex: |E|n|g|e|n|h|a|r|i|a|    |d| |e|   |S|o|f|t|w|a|r|e|
     0 1 2 3 4 5 6 7 8 9  10 11  12...
Cada caracter é salvo em um espaço diferente da memoria
Cada uma dessas caixas ocupa uma posição chamada de indice, como é mostrado a cima. Obs: até caracteres como espaço também ocupam espaço nessas micro memorias, e a contagem do indice é iniciada em 0.
----------------------------------------------------------------------------------------------------------------------------------
Dentro dessa assunto de String temos algumas tecnicas de manipulação de Strings, sendo elas:

fatiamento (texto[indice])
Análise com len(), count(), find()
transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().