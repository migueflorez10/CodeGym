# Inicio a la Programación orientada a obejtos

# Ejercicio - paradigma (Programacion estructurado)

clientes = [
    {'nombre': 'Miguel', 'apellido': 'Martinez', 'dni':'111111A'},
    {'nombre': 'Tomas', 'apellido': 'Marin', 'dni':'111111B'}
]

print(clientes)

def mostrar_clientes(clientes, dni):
    for c in clientes:
        if dni == c['dni']:
            print('{} {}'.format(c['nombre'], c['apellido']))
            return
    print('Usuario no encontrado')

mostrar_clientes(clientes, '111111A')

def borra_cliente(clientes, dni):
    for i,c in enumerate(clientes):  # toma indice, elemento de la lista cliente
        if dni == c['dni']:
            del(clientes[i])
            print('Se borro el cliente =>', str(c))
            return
    print('Cliente no encontrado')

borra_cliente(clientes, '111111A')
print('La lista actua es:', clientes)


# Mismo ejercico - Paradigma de programación orientada a objetos

class Cliente:
    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes
    
    def mostrar_clientes(self, dni = None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print('No se encontro el cliente')
        
    def borrar_cliente(self, dni = None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), '> BORRADO')
                return
        print('Cliente no encontrado')


miguel = Cliente(nombre = 'Miguel', apellidos = 'Martinez Florez', dni = '0000000A')
print(type(miguel))

juan = Cliente('Juan', 'Vera Lopez', '00000000B')

empresa = Empresa(clientes = [miguel, juan])
print(empresa.clientes)
print(empresa.mostrar_clientes(dni='0000000A'))
print(empresa.borrar_cliente(dni='00000000B'))
print(empresa.clientes)