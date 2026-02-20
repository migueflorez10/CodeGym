# Cadenas de texto - Metodos mas comunes

# upper() --> Convierte todo el texto a MAYÚSCULAS.
print('open ia es la empresa con mayor crecimiento en el mundo'.upper())

# lower() --> Convierte todo el texto a minúsculas.
print('NECESTIO RECIVAR EL PUNTO 3 SOBRE EL MODELO DE ALTO NIVEL DE LA ARQUIECTURA'.lower())

# capitalize() --> Convierte solo la primera letra en mayúscula y el resto en minúscula.
print('hola mundo'.capitalize())

# tittle() --> Convierte la primera letra de cada palabra en mayúscula.
print('eafit university'.title())

# count() --> Es para contar el numero de veces que aparece una letra/frase/palabra en la cadena de texto 
print('cccccccc aaaaaaa'.count('a'))

# find()--> Busca un texto y devuelve la posición (índice) donde aparece por primera vez.
print('hello world'.find('world'))

# rfind() --> Igual que find(), pero busca desde el final hacia atrás.
print('hello world world world world'.rfind('world'))

#isdigit() --> Devuelve True si todos los caracteres son números.
cadena = '123'
print(cadena.isdigit())

# isalnum() --> Devuelve True si el texto contiene solo letras y/o números (sin espacios ni símbolos).
cadena2 = 'ABC100bu'
print(cadena.isalnum())

# isalpha() --> Devuelve true si todos los valores de la cadena de texto son letras alfabeticas 
print('abcderfg'.isalpha())

# isupper() and islower() --> devuelve true si todos los valores de la cadena estan en minuscula o mayusculas
print('Hola como esta?'.isupper()) # no cumple 
print('muy bien y tu?'.islower()) # si cumple

# isspace() --> verifica si la cadena de texto esta llena de espacios 
print('      '.isspace())

#startwith() --> verifica si una cadena empieza con una letra o frase
print('Chat GPT es uno de los agentes de IA mas famosos del mundo'.startswith('Chat'))

#endtwith() --> verifica si una cadena termina con una letra o frase
print('Chat GPT es uno de los agentes de IA mas famosos del mundo'.endswith('mundo'))

# split() --> nos devuelve una lista con las palabras separas 
print('hello world welcome to muy code'.split()[-1])

# para separar por comas
print('code, programming, IA, bancked, frontend, data analyst'.split(','))

# join() --> Sirve para unir elementos de una lista en un solo string, usando un separador.
lista = ["Hola", "mundo"]
resultado = " ".join(lista)
print(resultado)

# strip() --> Sirve para eliminar espacios (u otros caracteres) al inicio y al final de un string.
texto = "   hola mundo   "
print(texto.strip())

# replace() --> Cambia un valor por otro dentro de la cadena de texto
print('hola mundo'.replace('o', '9'))