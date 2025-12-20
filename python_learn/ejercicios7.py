# 1) Realiza un programa que siga las siguientes instrucciones:
#     Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#     Crea un conjunto llamado administradores con los administradores Juan y Marta.
#     Borra al administrador Juan del conjunto de administradores.
#     Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
#     Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
# Notas: Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista.
# También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento.

usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Marta'}
administradores.discard('Juan')
print(administradores)
administradores.add('Marcos')

for u in usuarios:
    if u in administradores:
        print('El usuario: ', u, 'es administrador')
    else: 
        print('El usuario: ', u, 'no es administrador')
        


# **2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y
# balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes 
# cumplir las siguientes condiciones: **

#     El caballero tiene el doble de vida y defensa que un guerrero.
#     El guerrero tiene el doble de ataque y alcance que un caballero.
#     El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa 
#     y el doble de su alcance.
#     Muestra como quedan las propiedades de los tres personajes

caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

# El caballero tiene el doble de vida y defensa que el guerrero
caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

# El guerrero tiene el doble de ataque y alcance que el caballero
guerrero['ataque'] = caballero['ataque'] * 2
guerrero['alcance'] = caballero['alcance'] * 2

# El arquero tiene:
# - la misma vida y ataque que el guerrero
# - la mitad de defensa
# - el doble de alcance
arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

# Mostrar resultados
print('Caballero:', caballero)
print('Guerrero:', guerrero)
print('Arquero:', arquero)


