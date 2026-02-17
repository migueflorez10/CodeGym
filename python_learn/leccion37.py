# Uso y entendimiento del "self"

class Test:
    contador = 0 # atributo de clase (No pertenece a ningun objeto en especifico)
    
    def __init__(self):
        Test.contador += 1
        print(f'Instancias de Test creadas {Test.contador}')
    
for i in range(10):
    Test()
