# Encapsulamiento de atributos y metodos 

class Ejemplo: 
    __atributo_privado = 'Soy un atributo inalcanzable desde fuera'
    
    def __metodo_privado(self):
        return 'Soy un metodo inalcanzable desde fuera'
    
    def atributo_publico(self):
        return self.__atributo_privado
    
    def metodo_publico(self):
        return self.__metodo_privado()



e = Ejemplo()
print(e.atributo_publico())
print(e.metodo_publico())