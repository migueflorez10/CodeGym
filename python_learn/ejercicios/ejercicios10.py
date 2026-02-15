# Ejercicio 1: Realizar una funcion llamada area_rectangulo() que devuelva el area del cuadrado 
# a partie de una base  una altura. Calcular el area de un rectangulo de 15 de base y 10 de altura.

def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(15, 10))



# Ejercicio 2: Realizar una funcion llamada area_circulo() que devuelva el area de un circulo 
# a partir de un radio. calcula el area de un circulo de  5 deancho:
# NOTA: el area de un circulo se obtiene al elevar el radio a dos y multiplicando el resultado por pi: 3.14159 o
# importar el modulo math 

import math
def area_circulo(radio):
    return math.pi * (radio**2)

print(area_circulo(10))


# Ejercicio 3: Realizar una funcion llamada relacion() que a partir de dos numeros cumpla lo siguiente:
# Si el primer numero es mayor que el segundo, debe devolver 1
# Si el primer numero es menor que el segundo, debe devolver -1
# Si ambos numeros son iguales, debe devolver 0
# Comprueba las relaciones entre los numeros: '5 y 10', '10 y 5', '5 y 5'

def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0
    
print(relacion(10,5))
print(relacion(5,10))
print(relacion(5,5))


# Ejercicio 4: Realiza una funcion llamada intermedio() que a partir de dos numeros, devuelva su punto intermedio.
# NOTA: el numero intermedio entre dos numeros corresponde a la suma de los dos numeros dividido en 2 
# Comprueba el caso con -12 y 24

def intermedio(num1, num2):
    return (num1 + num2)/2

print(intermedio(-12, 24))



# Ejercicio 5: Realiza una funcion llamada recortar() que recibe tres parametros, el primero es el numero a recortar,
# el segundo es el limite inferior, y el tercero es el limite superior. La funcion tendra que cumplir lo siguiente: 
# Devolver el limite inferior si es numero es menor que este
# Devolver el limite superior si el numero es mayor que este 
# Devolver el numero sin cambios si no se supera ningun limite 


def recortar(num, limit_inf, limit_sup):
    if num < limit_inf:
        return limit_inf
    elif num > limit_sup:
        return limit_sup
    else: 
        return num
    
    
print(recortar(10,0,10))


# Ejercicio 6: Realizar una funcion separar() que tome una lista de numeros enteros y devuleva dos listas ordenadas. 
# La primera con los numeros pares, y la segunda con los numeros impares
# Ej: pares, impares = separar([6,5,2,1,7])
#     print(pares)
#     Print(Impares)
# Nota: Para ordenar una lista automaticamente usar el metodo sort()

numero = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares 
    

print(separar(numero))