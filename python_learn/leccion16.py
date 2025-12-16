# Lee un número entero n.
# Para todos los números no negativos i menores que n, imprime i² (i al cuadrado).
if __name__ == '__main__':
    n = int(input())

i = 0
while i < n: 
    print(i**2)
    i+=1
