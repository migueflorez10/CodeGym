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
