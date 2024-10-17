"""
2) Agregarle a la clase anterior un constructor que reciba nombre y edad. 

"""

class Persona():

    def constructor(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def identificarse(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

#creacion de personas

persona0 = Persona()
persona0.constructor("Raul", 22)

persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(26)

persona2 = Persona()
persona2.set_nombre("María")
persona2.set_edad(30)

persona0.identificarse()
persona1.identificarse()
persona2.identificarse()