""" Realizar un programa que conste de una clase llamada Alumno que tenga 
como atributos el nombre y la nota del alumno. Definir los métodos para 
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la 
nota y si ha aprobado o no. """

class Alumno: 

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return f"La nota de {self.nombre} es: {self.nota}"
    
    def verificar_nota(self):
        if self.nota >= 6:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}")
        else:
            print(f"{self.nombre} ha desaprobado con una nota de {self.nota}")



alumno1 = Alumno("juan", 8)
print(alumno1)

alumno1.verificar_nota()