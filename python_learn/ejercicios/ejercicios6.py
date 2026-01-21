# 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

#     Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#     Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#     Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#     Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#     Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).

print(list(range(0, 11)))
print(list(range(-10, 1)))
print(list(range(0, 21, 2)))
print(list(range(-19, 0 , 2)))
print(list(range(0, 51, 5)))


# 7) Dadas dos listas, debes generar una tercera con todos los elementos que se
# repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:

lista_1 = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]
lista_2 = ["h", "o", "l", "a", " ", "l", "u", "n", "a"]

lista_3 = []

for letra in lista_1: 
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)
print(lista_3)