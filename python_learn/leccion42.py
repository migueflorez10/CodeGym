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

# insert() --> Nos permite agregar elementos en una lista en el orden que yo quiera 
apple = ['ifhone', 'macbook air', 'macbook pro']
apple.insert(0,'ipad') # primero pasamos el indice que queremos y luego el valor 
print(apple)

# Si usamos el -1 en el insert, agregaremos un valor en el penultimo indice 
numeros = [5,10,15,25]
numeros.insert(-1,20)
print(numeros)
numeros.insert(6, 100)
print(numeros)

# pop() --> Nos permite sacar y eliminar elementos de una lista
carrito = ['leche', 'pan', 'queso', 'cafee']
carrito.pop(0)
print(carrito)

# remove() --> Elimina el valor que le pasemos de la lista 
# Nota: si los valores se repiten, unicamente borra el primero
productos = ['celular', 'TV', 'monitor', 'impresora 3d']
productos.remove('monitor')
print(productos)

# reverse() --> Devuelve la lista en modo contrario (alreves)
numbers = [1,2,3,4,5,6]
numbers.reverse()
print(numbers)

# reverse() + join() --> "reverse no existe en los str"

nombre = list('Miguel Angel')
nombre.reverse()
cadena = "".join(nombre)
print(cadena)

# sort() --> Organiza los elementos de una lista
precios = [10,2,30,0,29,40,32,50]
precios.sort()
print(precios)

# De mas grande a mas pequeño
precios.sort(reverse=True)
print(precios)