# Uso de la funcion input

Nombre = input('Escribe tu nombre: ')
edad = input('Escribe tu edad: ')
valor = float(input('Escribe un numero entero o decimal: '))
edad = int(edad)
print(edad+3)
print(valor)

# Ejercicio
nombre = input('Escribe tu nombre: ')
apellido = input('escribe tu apellido: ')
edad = int(input('Escribe un numero entero: '))
numero_magico = float(input('Escribe un numero decimal: '))
cadena_final = nombre + ' ' + apellido + ': Tu número de la suerte es el ' + str(edad*numero_magico)  