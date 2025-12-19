# Pilas y Colas (con listas)
from collections import deque #libreria para usar colas

pila = [1,2,3]
pila.append(4)
pila.append(5)
pila.append(6)
print(pila)
pila.pop()
print(pila)

cola = deque()
print(cola)
cola = deque(['Miguel', 'Angel', 'Martinez', 'Florez'])
print(cola.popleft())
print(cola)

