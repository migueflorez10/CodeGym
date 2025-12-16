# Operadores Logicos

# AND 
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('')
# OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('')
# Not
print(not True)
print(not False)
print('')


# Ejemplos con AND
print( 2==2 and (2*10)==20)
c = 'Hola Mundo'
print(len(c) >= 5 and c[0] == 'H')

print('')
# Ejemplos con OR
print( 2 > 9 or 9 == 10)
print( 2 > 9 or 10 == 10)

# Ejercicio 
# A partir de dos variables nombre  y edad crea una variable expresion que almacene 
# si se cumplen TODAS las siguientes condiciones encadenando operadores lógicos en una sola línea:
#Que nombre sea diferente de cuatro asteriscos.
#Que edad sea mayor que 10 y a su vez menor que 18.
#Que la longitud del nombre sea mayor o igual que 3 pero a la vez menor que 10

nombre = 'Miguel'
edad = 22
expresion = (nombre != '****') and (edad > 10 and edad < 18) and (len(nombre) >= 3 and len(nombre) < 10)