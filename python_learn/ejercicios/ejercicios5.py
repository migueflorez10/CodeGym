# # 5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que 
# mientras el número no sea correcto se repita el proceso. Luego debe comprobar si 
# el número se encuentra en la lista de números y notificarlo:

# Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se 
# encuentra en una lista (devuelve True o False)

numeros = [1, 3, 6, 9]

while True: 
    numero = int(input('Escribe un numero entre el 0 y el 9: '))
    if 0 <= numero <= 9:
        break
    elif numero > 9:
        print('El numero ingresado no es valido, intenta de nuevo')
        
if numero in numeros: 
    print('El numero', numero, 'se encuentra en la lista', numeros)
else: 
    print('El numero', numero, 'NO se encuentra en la lista', numeros)