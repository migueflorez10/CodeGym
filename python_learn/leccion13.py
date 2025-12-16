# Ejercicios 1

numero1 = float(input('Escribe un numero decimal: '))
numero2 = float(input('Escribe un segundo numero decimal: '))

print('Son iguales?', numero1==numero2)
print('Son diferentes?', numero1 != numero2)
print('El primero es mayor que el segundo?', numero1 > numero2)
print('El segundo es mayor o igual que el primero?', numero2 >= numero1)


print('')
# # Ejercicio 2

nombre = input('Escribe tu nombre: ')
condiciones = len(nombre)>=3 and len(nombre) < 10
print('La longitud de la cadena es mayor o igual que 3 y a su vez es menor que 10? ', condiciones)

# Ejercicio 3

numero_magico = 12345679
numero_usuario = int(input('Escribe un numero entre el 1 y el 9: '))
numero_usuario *= 9
numero_magico *= numero_usuario
print( 'El numero magico es: ', numero_magico)
