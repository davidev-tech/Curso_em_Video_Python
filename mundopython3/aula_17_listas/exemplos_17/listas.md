Listas assim como tuplas são variaveis compostas que guardam valores e seus valores são percorridos por indice. No entanto diferente das tuplas elas são mutaveis e recebem colchetes no inicio e fim: []
----------------------------------------------------------------------------------------------------------------------------------
Ex:  
        
lanches = ["Hamburguer", "Refrigerante", "Batata Frita", "Sorvete"]
lanches[0] = "Macarronada"
lanches = ["Macarronada", "Refrigerante", "Batata Frita", "Sorvete"]

O valor do indice 0 que era "Hamburguer" é substituido por "Macarronada"
----------------------------------------------------------------------------------------------------------------------------------
Comandos:

lista.append() Adiciona um novo elemento no final da lista
lista.insert(indice , elemento) Adiciona o novo elemento em um indice especificado.
del lista[indice] Deleta o elemento da lista na memoria.
del lista Deleta a lista toda da memoria.
lista.pop(indice) Remove um elemento da lista pelo indice.
lista.pop() Remove o ultimo elemento da lista.
lista.remove(item) Remove o elemento pelo valor.
lista.sort() ordena os valores.
lista.sort(reverse=True) ordena os valores no sentido inverso.
len(lista) Verifica o comprimento da lista, ou seja, quantos elementos tem dentro da lista.
----------------------------------------------------------------------------------------------------------------------------------Caso tente remover um elemento da lista que não existe a linguagem gera um erro. Para evitar tais problemas é sempre bom verificar.