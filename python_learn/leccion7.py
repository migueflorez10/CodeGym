# Ejercicio sobre listas
# Dadas dos listas lista1 y lista2 debes realizar diferentes tareas por el orden indicado:
#     Añade a la lista1 el número 1234 y luego el texto Hola.
#     Añade a la lista2 el texto Adiós y luego el número 1234.
#     Genera una lista3 con todos los elementos de la lista1 excepto el último.
#     Genera una lista4 con todos los elementos de la lista2 excepto el primero y el último.
#     Genera una lista5 con los elementos de la lista4 más la lista3.
# Los nombres de las variables deben ser los que se especifican o el ejercicio no validará.

# no modifiques el nombre de ninguna variable, puedes crear nuevas
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# completa el ejercicio
lista1.extend([1234, 'hola'])
print(lista1)

lista2.extend(['Adiós', 1234])
print(lista2)

lista3 = lista1[:-1]
print(lista3)

lista4 = lista2[1:-1]
print(lista4)

lista5 = lista4 + lista3
print(lista5)