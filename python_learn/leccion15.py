# Utilizando una condición if-elif-else debes realizar un programa que compare la longitud de dos variables
# (cadena_1 y cadena_2) y en función del resultado almacene un valor en otra variable llamada resultado:
#Si cadena_1 es más larga que cadena_2 la variable resultado deberá tener el valor entero 1.
#Si cadena_1 es más corta que cadena_2 la variable resultado deberá tener el valor entero 2.
#Si cadena_1 tiene la misma longitud que cadena_2 la variable resultado deberá tener el valor entero 0.

# Completa el ejercicio a partir de aquí

cadena_1 = 'Machine'
cadena_2 = 'Learning'

if (len(cadena_1) > len(cadena_2)):
    resultado = 1 
elif (len(cadena_1) < len(cadena_2)):
    resultado = 2 
else:
    resultado = 0
