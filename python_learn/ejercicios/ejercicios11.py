# 1) Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa 
# se bloquee y ademas explica mediante un mensaje al usuario la causa y/o solucion.

try:
    resultado = 10/0
except ZeroDivisionError:
    print('Error: no es posible dividir por 0, intenta con otro número')
    

# 2) Localizar el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee
# y ademas explica mediante un mensaje al usuario cual es la causa y/o solucion

lista = [1,2,3,4,5]
try:
    lista[10]
except IndexError:
    print('Error: El indice al que intentas acceder se encuentra fuera de rango', len(lista))
else: 
    print('El indice si existe dentro de la lista')


# 3) Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee
# y ademas explica mediante un mensaje al usuario cual es la causa y/o solucion

colores = {'rojo': 'red', 'verde':'green', 'azul':'blue'}
try:    
    colores['blanco']
except KeyError:
    print('Error: El valor clave de referencia no existe dentro del diccionario')


# 4) Localiza el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee
# y ademas explica mediante un mensaje al usuario cual es la causa y/o solucion

try:
    resultado = '20' + 15
except TypeError:
    print('Error: Solo es psoible sumar datos del mismo tipo, debes transformar el numero a cadena de texto o al reves')


# 5) Realiza una funcion llamada agregar_una_vez() que reciba una lista y un elemento. La funcion debe añadir el elemento 
# al final de la lista con la condicion de no repetir ningun elemento. Ademas si el elemento ya se encuentra en la lista 
# se debe invocar un error de tipo ValueError que debes capturar y mostrar el siguiente mensaje en su lugar.
# Error: imposible agregar elementos duplicados --> [elemento]
# Prueba agregando los elementos 10, -2, 'hola', a la lista de elementos con la funcion una vez la has creado y luego 
# muestra su contenido
# puedes usar la sintaxis : elemento in lista

elementos = [1, 5, -2]

def agregar_una_vez(lista, elemento):
    try: 
        if elemento in lista:
            raise ValueError
        else: 
            lista.append(elemento)
    except ValueError:
        print(f'Error: Imposible gregar elementos duplicados => [{elemento}]')

agregar_una_vez(elementos, 'hola')
agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
print(elementos)