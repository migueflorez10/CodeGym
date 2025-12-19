# Ejercicios de tuplas

tupla = (123,4, 2, 4, 1, 1, 'hola')

print(tupla[-1])
print(len(tupla)) # funcion len recorre los elementos de la lista y me dice cuantos hay
print(tupla.index(123))  # metodo index (busca un valor determinado) 
print(tupla[:3])
print(tupla[4])
print(tupla.count(4)) # el metodo count busca un varlor determinado y mira cuantas veces este valor se repite

# Ejercicios de conjuntos

conjunto = {1,2,3,4,5}
print(conjunto)

# Metodo add

conjunto.add(0)  # este valor deberia ponerse al final de la lista pero No, lo hace al inicio 
print(conjunto) # python internamente lo ordena como quiere


lista = [1,2,2,2,2,3,4,4,3,4] # lista con valores repetidos
lista = list(set(lista)) # convertimos esa lista a un set, el cual elimina dichos repetidos
print(lista)


# eje
# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
# Completa el ejercicio
for usuario in ["Ana", "Ramón", "Marta", "Eric", "David"]:
    grupo.add(usuario)
for usuario in ["Mario", "Miguel", "Ramón"]:
    grupo.remove(usuario)
    


# Dicccionarios (calve --> valor)
colores = {'Amarillo':'yellow', 'Verde': 'Green', 'Rojo': 'Red'}
print(colores)
colores['Amarillo'] = 'Gold' # Modifico el valor yellow por gold
print(colores)


edades = {'Miguel': 23, 'Liliana': 43, 'Aristarco': 48, 'Mateo': 22}
print(edades['Miguel'] + edades['Mateo'])

for edad in edades:  #accedemos unicamente a las claves mas no a los valores
    print(edad)
    

for claves in edades:
    print(edades[claves])

for claves in edades:
    print(claves, edades[claves])


for clave, valor in edades.items():   # items() devuleve pares como : 'Miguel':23
    print(clave, valor)


personajes = [
    {
        'nombre': 'Mario',
        'vida': 100,
        'nivel': 5,
        'arma': 'Salto'
    },
    {
        'nombre': 'Link',
        'vida': 120,
        'nivel': 8,
        'arma': 'Espada'
    },
    {
        'nombre': 'Kirby',
        'vida': 80,
        'nivel': 4,
        'arma': 'Absorber'
    }
]
