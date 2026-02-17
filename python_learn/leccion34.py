# Metodos especiales para las clases

class Pelicula: 
    # Constructor
    def __init__(self, nombre, duracion, lanzamiento):
        self.nombre = nombre
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f'Se ha creado una pelicula con el nombre: {self.nombre}')
    
    # Destructor de clase 
    def __del__(self):
        print(f'Se esta borrando la pelicula {self.nombre}')
    
    # Redefinimos el metodo string
    def __str__(self):
        return f'{self.nombre} lanzada en {self.lanzamiento}, con una duracion de: {self.duracion}'
    
    # Redefinimos el metodo length 
    def __len__(self):
        return self.duracion

maze_runner = Pelicula('Maze Runner', 120, 2017)
print(str(maze_runner))
print(len(maze_runner))

