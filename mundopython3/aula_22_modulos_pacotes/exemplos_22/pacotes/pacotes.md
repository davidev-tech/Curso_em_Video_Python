Pacotes são pastas que dentro deles possuem varios modulos, ou seja varios arquivos. Podemos ter pacotes dentro de um pacote, mas cada pasta deis da principal deve conter obrigatoriamente um arquivo __init__.py para que o pacote funcione normalmente. Na hora de importar, samos mais especicos. Usamos o from pacote import modulo
Ou seja va em pacote e importe esse modulo. Enquanto um modulo pode posuir varias funções um pacote pode possuir varios modulos.
----------------------------------------------------------------------------------------------------------------------------------
Hierarquia de Organização:
Função (Lógica) 
   └── Módulo (Arquivo .py)
         └── Pacote (Pasta com __init__.py)
               └── Biblioteca (Conjunto de Pacotes)