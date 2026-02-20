# listas - Metodos mas comunes

# append() --> agregar un elemento al final de la lista 

lista = [1,2,3,4,5]
lista.append(6)
print(lista)

# clear() --> Borra todos los elementos que conforman la lista
lista1 = [1,2,3]
lista1.clear()
print(lista1)

# extend() --> Une dos listas 
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

# count() --> Cuantas veces aparece un elemento en una lista 
lista2 = [1,2,3,4,4,5,5,5]
print(lista2.count(5))

# index() --> Es para buscar cual es la posicion de un elemento, como find() en las cadenas de texto
lista3 = ['hola', 'mundo', 'soy', 'miguel']
print(lista3.index('hola'))

