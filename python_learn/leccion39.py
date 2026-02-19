# Clases heredadas y polimorfismo
import copy 

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

class Libro(Producto):
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


ad = Adorno('0000A', 'Espejo estrella', 200000, 'Espejo estrella marca ikea')

ali = Alimento('00001', 'Carne de cerdo', 20000, '1 librad carne de cerdo' )
ali.productor = 'Pancho'
ali.distribuidor = 'proteccion'

lib = Libro('0000x', 'Alas de sangre', 130000, 'Libro mas vendido en reuno unido')
lib.isbn = '1029-2920282-19'
lib.autor = 'Rebecca Yarnos'

productos = [ad, ali]
productos.append(lib)

print(productos)

for p in productos:
    if (isinstance(p, Adorno)):
        print(p.referencia, p.nombre)
    elif (isinstance(p, Alimento)):
        print(p.referencia, p.nombre, p.distribuidor)
    elif (isinstance(p, Libro)): 
        print(p.referencia, p.nombre, p.autor)


def rebajar_producto(p, rebaja):
    # Devuelve un producto con una rebaja en porcentaje de su precio
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

ali_rebajado = rebajar_producto(ali, 10)
print(ali_rebajado)


# como copiar un objeto y por ende no hacer referencia de el
# importamos el modulo copy 

copia_adorno = copy.copy(ad)
copia_adorno.nombre = 'Espejo plano'
print(copia_adorno)
print(ad)
