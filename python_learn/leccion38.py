# Manejo de Herencias en POO 

class Producto():
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre 
        self.pvp = pvp
        self.descripcion = descripcion
    
    def __str__(self):
        return '''\
Referencia:\t{}
NOMBRE:\t\t{}
PVP:\t\t{}
DESCRIPCION:\t{}'''.format(self.referencia,self.nombre,self.pvp,self.descripcion)


class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ''
    distribuidor = ''

    def __str__(self):
        return '''\
Referencia:\t{}
NOMBRE:\t\t{}
PVP:\t\t{}
DESCRIPCION:\t{}
PRODUCTOR:\t{}
DISTRIBUIDOR:\t{}'''.format(self.referencia,self.nombre,self.pvp,self.descripcion, self.productor, self.distribuidor)

class Alimento(Producto):
    isbn = ''
    autor = ''

    def __str__(self):
        return '''\
Referencia:\t{}
NOMBRE:\t\t{}
PVP:\t\t{}
DESCRIPCION:\t{}
ISBN:\t\t{}
AUTOR:\t\t{}'''.format(self.referencia,self.nombre,self.pvp,self.descripcion, self.isbn, self.autor)


libro = Alimento('0005', 'El heroe de las eras', 120000, 'Tercer libro de la saga del cosmere')
libro.isbn = '0-830839-09-8'
libro.autor = 'Brandon Sanderson'
print(libro)

# lampara = Adorno('0001', 'Lampara de lava', 78000, 'Lampara de lava marca koop')
# print(lampara)


