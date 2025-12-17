# En este ejercicio se te facilitará un numero aleatorio que no conoces en la variable numero.
# Utilizando lo que conoces sobre los bucles for y la función range() , debes realizar un sumatorio de 
# todos los números desde 0 hasta ese numero (incluido) exceptuando los múltiples de 5 y 7, y almacenarlo 
# en la variable sumatorio.
numero = 12
sumatorio = 0

# Completa el ejercicio aquí

for i in range(0, numero + 1):
    if ((i % 5) == 0 or (i % 7) == 0):
        continue
    sumatorio +=i