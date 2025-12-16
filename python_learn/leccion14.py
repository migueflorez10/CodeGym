# Flujos / Condicionales / Iteraciones

# Ej 1
if True:
    print('Primer flujo')

# Ej 2
a = 5
if (a == 5):
    print('a vale 5')
else:
    print('a es diferente de 2')

# Ej 3 --> if dentro de otro if
b = 4
c = 7
if (b == 4):
    print('El valor de b es: ', b)
    if(c > 4):
        print('El valor de c es mayor a 4')
        
        
n = 11 
if (n % 2) == 0:
    print(n, 'Es un numero par')
else: 
    print(n, 'Es un numero impar')
    
    
# Ej 4 --> Uso de if, else, elif
comando = 'Salir'

if (comando == 'Entrar'):
    print('Bienvenido al sistema')
elif (comando == 'Saludar'):
    print('Saludo Usuario')
elif (comando == 'Salir'):
    print('Saliendo del sistema')
else:
    print('Comando no valido')
    
    
    
# Ej 5 

nota_final = float(input('Escribe tu nota final: '))

if (nota_final == 10):
    print('Tu nota fue sobresaliente')
elif(nota_final == 9 or nota_final >= 7):
    print('Tu nota es buena')
elif (nota_final == 6):
    print('Tu nota es suficiente')
else:
    print('Tu nota es insuficiente')

