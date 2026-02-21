# Conjuntos - metodos mas comunes

# add() --> Nos permite agregar un elemento dentro de nuestro conjunto
c = set()
c.add(1)
c.add(2)
c.add(3)
print(c)

# discard() --> Nos permite descartar o eliminar un elemento dentro de nuestro conjunto
c.discard(3)
print(c)

# copy()--> Nos permite copiar un conjunto dentro de otro conjunto
c2 = c.copy()
c2.add(3)
c2.add(4)
c2.add(5)
print(c2)

# clear() --> Vacia los elementos de una lista 
c2.clear()
print(c2)

# Comparaciones
conjunto1 = {1,2,3}
conjunto2 = {3,4,5}
conjunto3 = {-1,99}
conjunto4 = {1,2,3,4,5}

# isjisjoint() --> Sirve para saber si dos conjuntos NO tienen ningún elemento en común.
print(conjunto1.isdisjoint(conjunto3))

# issubset() --> ¿Todos los elementos de conjunto1 están dentro de conjunto4?
print(conjunto1.issubset(conjunto4))
print(conjunto2.issubset(conjunto4))

# issuperset() --> ¿conjunto4 contiene TODOS los elementos de conjunto1?
print(conjunto4.issuperset(conjunto1))

# union() --> Sirve para unir todos los elementos de ambos conjuntos en uno solo.
print(conjunto1.union(conjunto2)== conjunto4)

# update() --> Es como agarrar tu hoja actual y escribirle encima lo nuevo.
conjunto1.update(conjunto2)
print(conjunto1)

# difference() --> "Lo que tengo yo y tú no.”
print(conjunto1.difference(conjunto3))

# difference_update() --> Quitar del conjunto actual todos los elementos que estén en otro conjunto.
print(conjunto1.difference_update(conjunto2))

# intersection() --> Obtener los elementos que están en ambos conjuntos al mismo tiempo.
print(conjunto1.intersection(conjunto2))

# 