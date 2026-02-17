# Objetos dentro de objetos

class Pelicula():
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f'Se ha creado la pelicula: {self.titulo}')
    
    def __str__(self):
        return f'la pelicula: {self.titulo} , fue lanzada el año: {self.lanzamiento} '

class Catalogo():
    peliculas = []
    def __init__(self, peliculas = []):
        self.peliculas = peliculas

    def agregar_peliculas(self, p):
        self.peliculas.append(p)
    
    def mostrar_peliculas(self):
        for p in self.peliculas:
            print(p)

p = Pelicula('Red Rising', 160, 2028)
c = Catalogo([p])
c.agregar_peliculas(Pelicula('Golden son', 130, 2030))