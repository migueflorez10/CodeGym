# En este ejercicio vamos a trabajar el concepto de puntos, coordenadas y vectores sobre el plano cartesiano y como 
# la programacion orientada a objetos puede ser una excelente aliada para trabajar con ellos. No esta pensado para
# que hagamos ningun tipo de calculo sino para que practiquemos la automatizacion de tareas.

# NOTA: El plano cartesiano, representa un espacio bidimensional (en 2 dimensiones), formado por dos rectas 
# perpendiculares, una horizontal y otra vertical que se cortan en un punto. La recta horizontal se denomina
# eje de las obcisas o eje x, mientras que la vertical recibe el nombre de eje de las ordenadas o eje y. En cuanto 
# al punto donde se cortan, se conoce con el punto de origen 0.

import math

class Punto:
    # Constructor que tomara dos coordenadas 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 
    
    def __str__(self): # el metodo srt define como se ve un objeto cuando se imprime
        return f'{self.x}, {self.y}'
        
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print(f'{self} pertenece al primero cuadrante')
        elif self.x < 0 and self.y > 0:
            print(f'{self} pertenece al segundo cuadrante')
        elif self.x < 0 and self.y < 0:
            print(f'{self} pertenece al tercer cuadrante')
        elif self.x > 0 and self.y < 0:
            print(f'{self} pertenece al cuarto cuadrante')
        else: 
            print(f'{self} se encuentra sobre el origen')
    
    def vector(self, p):
        print(f'El vector entre {self} y {p} es: ({p.x - self.x, p.y - self.y})')
    
    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y-self.y)**2)
        print(f'La distancia entre los puntos: {self} y {p} es de: {d}')


class Rectangulo():
    def __init__(self, pInicial = Punto(), pFinal = Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
    
    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print(f'La base del rectangulo es: ({self.base})')
    
    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print(f'La altura del rectangulo es: ({self.altura})')
        
    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        print(f'El area del rectangulo es: ({self.area})')

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Consulta de los Cuandrantes de cada punto
# A.cuadrante()
# C.cuadrante()
# D.cuadrante()

# Consultar el vector 
# A.vector(B)
# B.vector(A)

# Consultar la distancia entre dos puntos 
# A.distancia(B)
# B.distancia(A)

# Determinar cual de los tres puntos A,B o C, se encutra mas lejos de origen, punto (0,0)
# A.distancia(D)
# B.distancia(D)
# C.distancia(D)

# creamos un rectnagulo

R = Rectangulo(A, B)

R.base()
R.altura()
R.area()



