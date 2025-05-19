#list comprehension em python

#forma rápida de criar listas a partir de iteráveis. 

#|____#|#____#|#____#|#____#|#____#|#____#|#____#|#____#|#____#|#

#lista = [] #criando uma lista

#for i in range(10): #para cada i, é adicionado ao lista
 #   lista.append(i) 
#print(lista) #mostra a lista no terminal.and

lista = [

    numero * 2
    for numero in range(10)
    
]

print(lista)


