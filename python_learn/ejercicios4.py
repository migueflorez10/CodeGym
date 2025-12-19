# 3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
# Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer 
# parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

print(sum(range(0, 101, 2)))

# Segunda opcion: 
num = 0 
suma = 0 

while num <= 100:
    if (num % 2) == 0:
        suma += num
    num += 1
print(suma)


# 4) Realiza un programa que pida al usuario cuantos números quiere introducir. 
# Luego lee todos los números y realiza una media aritmética:

cantidad = int(input('Cuantos numeros quieres introducir: '))
acumulador = 0 

for i in range(cantidad):
    numero = int(input('Escribe un numero: '))
    acumulador += numero
resultado = acumulador / cantidad
print('El resultado es: ', resultado)   


