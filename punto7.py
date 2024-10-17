""" Desarrollar un programa que cargue los datos de un triángulo. Implementar una 
clase con los métodos para inicializar los atributos, imprimir el valor del lado 
con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o 
escaleno).  """

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor_lado(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado de mayor tamaño es: {mayor}")

    def tipo_triangulo(self):

        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")
        

#triangulos
triangulo1 = Triangulo(5,5,5)
triangulo2 = Triangulo(2,9,9)
triangulo3 = Triangulo(23,12,2)

# Mostrar lado mayor y clase de triangulo
triangulo1.mayor_lado()
triangulo1.tipo_triangulo()

triangulo2.mayor_lado()
triangulo2.tipo_triangulo()

triangulo3.mayor_lado()
triangulo3.tipo_triangulo()