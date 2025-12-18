# Bucles anidados

lista = [
    'Esto es un texto',
    (1,2,3,4,5,6,7,8,8,19),
    ['Azul', 'Verde', 'Rojo']
]

# for i in lista:
#     print(i)


for coleccion in lista:
    for elemento in coleccion:
        print(coleccion, '-->', elemento)



# Otro ejemplos
tabla = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for fila in tabla:
    for columna in fila:
        print(columna, end='')
    print()
    


# En este ejercicio se te va a facilitar una variable matriz repleta de números enteros y 
# de la cuál lo único que sabes es que contiene dos dimensiones.
# Aquí tienes una estructura de ejemplo ilustrando como se forma (lista con sublistas), 
# muy parecida a una tabla:
    matriz = [
        [8,  7,  0],
        [34, 2, -1],
        [5, -5, 12]
    ]

# Primero recorremos todas las filas de la matriz con un for
# Necesitamos usar un enumerador para poder guardar su índice de fila
for i, fila in enumerate(matriz):
    # Dentro de cada fila recorremos cada columna con otro for
    # Necesitamos usar un enumerador para poder guardar su índice de columna
    for j, columna in enumerate(fila):
        # A partir de ambos índices podemos comprobar la celda actual
        # Si es par asignamos a la celda un 0
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        # En caso contrario, si es impar, le asignamos un 1
        else:
            matriz[i][j] = 1