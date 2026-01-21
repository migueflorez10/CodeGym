# Argumentos y parametros Indeterminados

def indeterminados_pisicion(*args):
    for i in args:
        print(i)

indeterminados_pisicion(7, 'Bienvenido', [12,22,34])

#--------------------------------------------------------#

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, ' ', kwargs[kwarg])

indeterminados_nombre(n=7, c='Bienvenido', l=[12,22,34])

#--------------------------------------------------------#

def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t+= arg
    print('El sumatorio indeterminado es: ', t)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

super_funcion(10,10,10,10,10,50,100, nombre = 'Miguel', edad = 32)