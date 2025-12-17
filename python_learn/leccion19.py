# Uso de while y for 

numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0 

# while (indice < len(numeros)):
#     print(numeros[indice]) #Dame el elemento de la lista numeros que está en la posición indice
#     indice+=1
    
    
# for numero in numeros: 
#     print(numero)
    
    

# for numero in numeros: 
#     numeros[indice] *= 10
#     indice +=1
# print(numeros)

for indice, numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)


cadena = 'Miguel'
for caracteres in cadena: 
    print(caracteres)
    
    
for i in range (10):
    print(i)