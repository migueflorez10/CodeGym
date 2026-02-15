# Multiples excepciones

try:
    n = float(input('Escribe un número: '))
    5/n
except TypeError:
    print('No se puede dividir un numero con una cadena de texto')
except ValueError: 
    print('El valor ingresado es invalido, porfavor digita un número')
except ZeroDivisionError:
    print('No se puede realizar una divion sobre 0, intenta con otro número')
except Exception as e: # guardamos el error en la variable e 
    print(type(e).__name__) # mostramos el typo de error



# Invocacion de excepciones 

def funcion_prueba(algo = None):
    try:
        if algo is None:
            raise ValueError('El valor ingresado no puede ser nulo')
    except ValueError:
        print('El valor ingresado no puede ser nulo, DESDE LA EXCEPCION')


print(funcion_prueba())
