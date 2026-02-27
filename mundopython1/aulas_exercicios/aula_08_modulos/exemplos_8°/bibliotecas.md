bibliotecas são conjutos de funcionalidades prontas que não veem nativamente na linguagem.

Essas funcionalidades não nativas devem ser importadas por meio de bibliotecas, na qual ja tem as funcionalidades desejadas desenvolvidas para o desenvolvimento de funções especificas dentro do sistema.

A importação de bibliotecas no Pyton ocorre por meio do comando import + nome do módulo ou biblioteca. Obs: essas importações devem ocorrer logo no inicio do progama.

----------------------------------------------------------------------------------------------------------------------------------
Ex: import + biblioteca irá importar toda a biblioteca.

    from biblioteca import + item especifico irá importar apenas um item especifico.

----------------------------------------------------------------------------------------------------------------------------------
A biblioteca math é a biblioteca matemática do Python.

comandos de arredondamento da respectiva biblioteca:

ceil é o comando para arredondar o valor para cima.
floor é comando para arredondar o valor para baixo.
trunc é o comando que irá truncar um número elimirar da virgula para frente.
pow é a comando para calcular potencia.
sqrt é o comando para calcular raiz.
factorial é o comando para calcular calculos fatoriais.
----------------------------------------------------------------------------------------------------------------------------------
Tomando como referencia os exemplos anteriores.

import math iria importar toda a biblioteca matemática.
from math import sqrt importaria somente a função para raiz quadrada.

Caso queira importar mais de uma funcionalidade especifica é nescessario sepera las por virgula. 
Ex: From math import sqrt, pow importaria tanto a função para calcular raiz, quanto a função para calcular calcular potencia.
----------------------------------------------------------------------------------------------------------------------------------
Para usar bibliotecas externas, primeiro é nescessario instalar a biblioteca na sua maquina, só depois disso é possivel importar a biblioteca usando normalmente como nos exemplos anteriores.