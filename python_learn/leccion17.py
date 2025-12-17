# Bucle While

c = 0 
while (c <= 5):
    c += 1
    if(c == 2):
        print('Rompemos el bucle cunado c vale', c)
        break
    print('El valor de C es: ', c)
else: 
    print('Se ha completado la iteracion')
    
    
# Uso de break
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1


# Uso de continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
