# Manejo de excepsiones en pyhton

while(True):
    try: # captura el error
        n = float(input('Escribe un numero: '))
        m = 10
        print('{}/{}:{}'.format(n,m,n/m))
    except: # definir el codigo excepcional
        print('Escribe bien el numero requerido')
    else: # definir cuando no ocurre ningun error 
        print('Todo ha funcionado de manera correcta')
        break # importante romper la iteracion si todo ha salido bien 
    finally: # definir el codigo que se ejeuctara al final exista o no exista ningun error
        print('Fin de la iteracion')
        
