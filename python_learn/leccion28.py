# Funciones Recursivas

# No devolvemos un valor por medio de un return
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else: 
        print('Booooooom')
    print('Fin de la funcion', num)

cuenta_atras(5)


# devolvemos un valor por medio de un valor return
def factorial(num):
    print('Valor inicial --> ', num)
    if num > 1:
        num = num * factorial(num -1)
    print('Valor final --> ', num)
    return num

print(factorial(5))



# Ejercicio
# Completa el ejercicio
def sumatorio(numero):
    if numero > 1:
        numero = numero + sumatorio(numero - 1)
    return numero
    
print(sumatorio(5))