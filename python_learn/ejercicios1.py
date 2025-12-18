# Se te da un número n.
# Debes calcular la suma de todos los números desde 0 hasta n (incluido),
# excepto:
# los números pares
# 📌 Guarda el resultado en una variable llamada resultado.
# 🔎 Pista:
# Piensa cómo detectar si un número es par usando %.

n = int(input('Escribe un numero entero entre el 0 y el 10: '))
resultado = 0
for i in range (0, n + 1):
    if ((i % 2) == 0):
        continue
    resultado += i
    print(resultado)
    
    
# Dado un número n, recorre los números desde 1 hasta n (incluido) y:
# cuenta cuántos números son múltiplos de 3
# guarda el total en una variable llamada contador
# 📌 No sumes los números, solo cuéntalos.

n = int(input('Escribe un numero del entero: '))
contador = 0
for i in range (1, n + 1):
    if ( (i % 3) == 0):
        contador += 1
print(contador)


# Recorre los números del 1 al 50.
# Ignora (no muestres) los múltiplos de 4
# Muestra por pantalla solo los que sí se procesan
# 📌 Usa un for.

for i in range (1, 50 + 1):
    if ((i % 4) == 0):
        continue
    else: 
        print(i)