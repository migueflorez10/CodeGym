# Programacion orientada a objetos 

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre 
        self.fuerza = fuerza 
        self.inteligencia = inteligencia
        self.defensa = defensa 
        self.vida = vida 
    
    def atributos(self):
        print(self.nombre, ':', sep="")
        print('Fuerza:', self.fuerza)
        print('Inteligencia:', self.inteligencia)
        print('Defensa:', self.defensa)
        print('Vida:', self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def esta_muerto(self):
        self.vida = 0
        print(self.nombre, ' :Ha muerto')
    
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f'{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}')
        print(f'la vida de {enemigo.nombre} es de {enemigo.vida}')

mi_personaje = Personaje('Darrow Of Likos', 99, 80, 90, 100)
mi_enemigo = Personaje('Adrius Lun', 80, 90, 80, 100)

print(f'los atributos de mi personaje son: {mi_personaje.atributos()}')
print(mi_personaje.daño(mi_enemigo))