"""  En un banco tienen clientes que pueden hacer depósitos y extracciones de 
dinero. El banco requiere también al final del día calcular la cantidad de dinero 
que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase 
banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos 
__init__, depositar, extraer, mostrar_total. La clase banco tendrá como 
atributos 3 objetos de la clase cliente y los métodos __init__, operar y 
deposito_total.  """

class Cliente:

    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, monto):
            self.cantidad += monto
            print(f"{self.nombre} ha depositado {monto}. Saldo actual: {self.cantidad}")

    def extraer(self, monto):
        if monto <= self.cantidad:
             self.cantidad -= monto
             print(f"{self.nombre} ha extraído {monto}. Saldo actual: {self.cantidad}")
        else:
             print(f"{self.nombre} no tiene suficiente saldo para extraer {monto}")
    
    def mostrar_total(self):
         print(f"{self.nombre} tíene un saldo total de: {self.cantidad}")
         return self.cantidad
    

class Banco:
     
    def __init__(self):
          self.clientes = [
               Cliente("Juan"),
               Cliente("Ana"),
               Cliente("Pedro")
          ]
    
    def añadir_cliente(self, cliente):
         self.clientes.append(cliente)

    def operar(self):
        print("/n---- Operaciones ----")
        self.clientes[0].depositar(11000)
        self.clientes[1].depositar(6000)
        self.clientes[2].extraer(500)

    def deposito_total(self):
        total = sum(cliente.mostrar_total() for cliente in self.clientes)
        print(f"\nEl total depositado en el banco es: {total}")


banco = Banco()
banco.operar()
banco.deposito_total()