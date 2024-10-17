""" Realizar un programa en el cual se declaren dos valores enteros por teclado 
utilizando el método __init__. Calcular después la suma, resta, multiplicación y 
división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.  """

class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def sumar(self):
        return self.valor1 + self.valor2
    
    def restar(self):
        return self.valor1 - self.valor2

    def multiplicar(self):
        return self.valor1 * self.valor2
    
    def dividir(self): 
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "no se puede dividir entre 0"
        

valor1 = int(input("Introducir el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))

calculadora = Calculadora(valor1, valor2)

print(f"Suma: {calculadora.sumar()}")
print(f"Resta: {calculadora.restar()}")
print(f"Multiplicación: {calculadora.multiplicar()}")
print(f"División: {calculadora.dividir()}")