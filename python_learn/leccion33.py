# La clase es un molde para crear galletas

class Galletas():
    pass

una_galleta = Galletas()
otra_galleta = Galletas()

print(type(una_galleta))


# Atributos y Metodos de clase 

class Pizza():
    pass

pizza_hawaiana = Pizza()
pizza_carne = Pizza()

pizza_hawaiana.sabor = 'Hawaiana'
pizza_hawaiana.precio = 3000

pizza_carne.sabor = 'carne'
pizza_carne.precio = 3200

print('El precio de esta pizza es: ', pizza_hawaiana.precio)
print('El precio de esta pizza es: ', pizza_carne.precio)


# Uso de __init__ y self 

class Cookies():
    chocolate = False
    def __init__(self, sabor = None, color = None): # __init__ es un metodo especial de una clase
        self.sabor = sabor 
        self.color = color
        if sabor is not None and color is not None:
            print(f'Se acaba de crear una cookie {sabor} y {color}')
    
    def chocolatear(self):
        self.chocolate = True
    
    def tiene_chocolate(self):
        if (self.chocolate):
            print('Soy una cookie chocolateada :) ')
        else:
            print('Soy una cookie sin chocolate :( ')


# c = Cookies()
# g = Cookies()
# g.tiene_chocolate()
# g.chocolatear()
# g.tiene_chocolate()

b = Cookies('dulce', 'roja')
b1 = Cookies('salada', 'blanca')

