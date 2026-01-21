#  03 Control de flujos
# 1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#     Mostrar una suma de los dos números
#     Mostrar una resta de los dos números (el primero menos el segundo)
#     Mostrar una multiplicación de los dos números
#     En caso de no introducir una opción válida, el programa informará de que no es correcta.
numero1 = int(input('Escoge un primer numero: '))
numero2 = int(input('Escoge un segundo numero: '))

while True: 
    print(""" 
        1) Mostrar una suma de los dos números
        2) Mostrar una resta de los dos números (el primero menos el segundo)
        3) Mostrar una multiplicación de los dos números
        4) Volver a seleccionar ambos numeros
        """)
    opcion = input('Selecciona una opcion del menu: ')
    if (opcion == '1'):
        print('La suma de los dos numero es: ', (numero1 + numero2))
    elif (opcion == '2'):
        print('La resta de los dos numeros es: ', (numero1 - numero2))
    elif (opcion == '3'):
        print('La multiplicacion de los dos numeros es: ', (numero1 * numero2))
    elif (opcion == '4'):
        break
    else: 
        print('La opcion del menu es incorrecta')


# # 2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número 
# # impar, debe repetise el proceso hasta que lo introduzca correctamente.

numero = 0
while (numero % 2) == 0:
    numero = int(input('Escribe un numero impar: '))