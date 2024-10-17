"""  Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva 
True o False.  """


class Persona():

    mayoriaEdad = False

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

    def es_mayor_de_edad(self):
        if(self.edad > 18):
            self.mayoriaEdad = True
            print(f"{self.nombre} es mayor de edad")
        else:
            self.mayoriaEdad = False
            print(f"{self.nombre} es menor  de edad")

#creacion de personas

persona0 = Persona()
persona0.constructor("Raul", 14)

persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(26)

persona2 = Persona()
persona2.set_nombre("María")
persona2.set_edad(30)

persona0.identificarse()
persona0.es_mayor_de_edad()
persona1.identificarse()
persona1.es_mayor_de_edad()
persona2.identificarse()
persona2.es_mayor_de_edad()