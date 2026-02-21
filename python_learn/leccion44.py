# Diccionarios - Metodos mas comunes

colores = {'amarillo':'yellow', 'azul':'blue', 'rojo':'red'}
print(colores['amarillo'])

# get() --> Obtener el valor de una clave sin que el programa falle si la clave no existe
print(colores.get('verde', 'No existe'))
print('negreo' in colores) # otra forma rapida de saber si una clave se encuentra dentro del diccionario

# keys() --> Obtener todas las claves del diccionario
print(colores.keys())

# values() --> Obtener todos los valores del diccionario
print(colores.values())

# items() --> Obtener las claves y los valores al mismo tiempo
print(colores.items())

# iterar diccionarios
for c in colores.keys():
    print(c)

for c in colores.values():
    print(c)

for c,v in colores.items():
    print(c,v)

# pop() --> Elimina la clave y el valor de un diccionario
print(colores.pop('verde', 'No existe'))

# clear() --> Vacia el diccionario
colores.clear()
print(colores)


