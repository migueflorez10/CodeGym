class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    
# Completa el ejercicio aquí

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga ):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", {} Kg".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ", tipo: {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


coche = Coche('Rojo', 2 , '1500', '800')
camioneta = Camioneta('Blanca', 4, '1200', '1000', '100')
bicicleta = Bicicleta('Negro', 2, 'Deportiva')
motocicleta = Motocicleta('Azul', 2, 'Urbana', '1600', '300')

vehiculos = [coche, camioneta, bicicleta, motocicleta]
print(vehiculos)

def catalogar(vehiculos):
    for i in vehiculos:
        print(type(i).__name__,':', i)

catalogar(vehiculos)

    
def catalogar(vehiculos, ruedas = None):
    # Primero, mostrar recuento del numero de ruedas
    if ruedas != 0:
        contador = 0
        for r in vehiculos:
            if r.ruedas == ruedas:
                contador += 1
        print(f'\nSe han encontrado {contador} vehiculos con {ruedas}:')
    # Mostrar vehiculos 
    for r in vehiculos:
        if ruedas == None:
            print(type(r).__name__, r)
        else: 
            if r.ruedas == ruedas:
                print(type(r).__name__, r)

catalogar(vehiculos)
catalogar(vehiculos, 0)
catalogar(vehiculos, 2)
catalogar(vehiculos, 4)