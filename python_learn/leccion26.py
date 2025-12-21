# Programacion de funciones
def saludar():
    print('Hola Mundo')

saludar()

def tabla_del_cinco():
    for i in range(11):
        print('5 * ', i, ' es:', (i * 5))

tabla_del_cinco()


# Retorno de variables
def test():
    return 'una cadena retornada' # el return es como un break, aqui termina la ejecucion de la funcion

print(test())
c = test()
print(c)

# uso de slicing en una funcion
def lista():
    return [1,2,3,4,5,6,7,8,9,10]

print(lista()[:3])
print(lista()[-1])


# Retornar multiples valores por comas en una funcion
def test2():
    return 'Miguel', 22, [10,20,30]

print(test2())

c, n, l = test2()

print(c)
print(n)
print(l)

# Como reciben informacion las funciones ? 
def suma(a,b):
    return a + b

print(suma(5,5))


# Ejercicio: 
def par_o_impar(numero):
    if numero % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')


# Ejercicio 2
# Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres argumentos:

#     El primero es el número a recortar

#     El segundo es el límite inferior

#     El tercero el límite superior. 

# La función tendrá que cumplir lo siguiente:

#     Devolver el límite inferior si el número es menor que éste

#     Devolver el límite superior si el número es mayor que éste.

#     Devolver el número sin cambios si no se supera ningún límite.

# Completa el ejercicio

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else: 
        return numero