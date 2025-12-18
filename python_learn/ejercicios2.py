# EJERCICIO 4 – while hasta que se cumpla la condición
# Pide números por teclado una y otra vez hasta que el usuario introduzca:
# un número múltiplo de 6
# Cuando lo haga, muestra:
# Correcto, es múltiplo de 6
# 📌 Usa while.

while True:
    numero = int(input('Escribe un numero: '))
    if ((numero % 6) == 0):
        print('Correcto, es múltiplo de 6')
        break


# EJERCICIO 5 – Sumatorio con doble exclusión (nivel exacto al que hiciste)
# Dado un número n, calcula la suma de los números desde 1 hasta n (incluido),
# exceptuando:
# múltiplos de 3
# múltiplos de 5
# 📌 Guarda el resultado en sumatorio.
# 🔎 Pista:
# Ojo con el operador lógico que uses (and / or).

n = int(input('Escribe un numero: '))
sumatorio = 0
for i in range (1 , n + 1):
    if ((i % 3) == 0 or (i % 5) == 0):
        continue
    sumatorio += i
print(sumatorio)