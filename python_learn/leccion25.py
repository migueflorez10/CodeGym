# Entradas y Saalidas

valores = [
    
]
print('Introduce 3 valores: ')
for i in range(3):
    valores.append(input('Escribe un valor: '))
print('La lista contiene los siguientes valores: ', valores)


import sys # permite usar argumentos desde la terminal

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for r in range(repeticiones):
        print(texto)
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: escribir_lineas.py "Texto" 5')


# Salidas
# Formateo de cadenas (String Formatting)
v = "otro texto"
n = 10

c = "Un texto '{}' y un número '{}'".format(v, n) # usamos el metodo format
print(c)

# Nota: format() --> Sirve para nsertar, ordenar, dar formato y presentar datos dentro de un texto.

# posicion de indices 
"{1} - {0}".format("A", "B")

# Usar nombres (MUY claro y profesional)
"{nombre} tiene {edad} años".format(nombre="Miguel", edad=23)

# Guardar el texto formateado en una variable
mensaje = "Hola {}, bienvenido".format("Miguel")
print(mensaje)

# Alineamiento de una palabra a la derecha (30 caracteres)
print('{:>30}'.format('Miguel'))

# Alineamiento de una palabra al centro (30 caracteres)
print('{:^30}'.format('Angel'))

# Truncamiento a 3 caracteres
# Alineamiento de una palabra a la derecha (30 caracteres)
print('{:.3}'.format('Miguel'))

# Alineamiento a la derecha con truncamiento de 3 caracteres
print('{:>30.3}'.format('Miguel'))

# Formateo de numero enteros, rellando con espacios
print('{:4d}'.format(10))
print('{:4d}'.format(100))
print('{:4d}'.format(1000))

# Formateo de numero enteros, rellando con ceros 
print('{:04d}'.format(10))
print('{:04d}'.format(100))
print('{:04d}'.format(1000))

# formateo de numeros decimales, rellenado con espacios
print('{:7.2f}'.format(3.1415926))
print('{:7.2f}'.format(153.21))

# formateo de numeros decimales, rellenado con ceros
print('{:07.2f}'.format(3.1415926))
print('{:07.2f}'.format(153.21))


# Otra forma de insertar texto en una cadena SIN usar format es la siguiente:

nombre = 'Miguel'
cadena = f'hola {nombre}'
print(cadena)

a = 10
b = 5

print(f"La suma es {a + b}")
print(f"El doble de a es {a * 2}")


# Formateo de numeros
pi = 3.14159265

print(f"Pi con 2 decimales: {pi:.2f}")
print(f"Pi con 4 decimales: {pi:.4f}")


# Sepradador de miles
numero = 123456789

print(f"Numero grande: {numero:,}")


# Alineacion 
nombre = "Angel"

print(f"|{nombre:<20}|  Izquierda")
print(f"|{nombre:^20}|  Centro")
print(f"|{nombre:>20}|  Derecha")

# Alineacion con relleno 
nombre = "Angel"

print(f"|{nombre:*^20}|")
print(f"|{nombre:_<20}|")
print(f"|{nombre:.>20}|")


# Uso con diccionarios
persona = {
    "nombre": "Juan",
    "edad": 30
}

print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")

# Uso con bucles
for i in range(1, 6):
    print(f"Numero: {i}")
