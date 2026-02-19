# Herencia Multiple 

class A():
    def __init__(self):
        print('Soy de clase A')
    def a(self):
        print('Este metodo lo heredo de A')

class B():
    def __init__(self):
        print('Soy de clase B')
    def b(self):
        print('Este metodo lo heredo de B')


class C(A,B):
    def c(self):
        print('Este metodo es propio')

c = C()
print(c.a())
print(c.b())
print(c.c())

