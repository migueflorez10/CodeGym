# Ejericio de interfaz interactiva usando el bucle while

print('Bienvenido al menu principal')
while True: 
    print("""Que quieres hacer? Elige una opcion:
        1) Saludar
        2) Sumar dos numeros
        3) Salir del programa""")
    opcion = input()
    if (opcion == '1'):
        print('Bienvenido Usuario, espero este sistema de ayude mucho en tu progreso')
    elif (opcion == '2'):
        num1 = float(input('Escribe el primer numero: '))
        num2 = float(input('Escribe el segundo numero: '))
        print('La suma de los dos numeros es: ', (num1+num2))
    elif (opcion == '3'):
        print('Saliendo del programa....')
        break
    else: 
        print('Opcion no valida, intenta de nuevo')
        
        
        
# Realiza un programa que lea un número por teclado y lo almacene en una variable llamada numero.
# Si ese número introducido por teclado no es múltiple de 5 debe repetirse de nuevo la lectura hasta que lo sea.

numero = int(input())

while ((numero % 5) !=0 ):
    numero = int(input('Intenta con otro numero: '))
