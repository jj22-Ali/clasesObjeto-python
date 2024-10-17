""" Realizar una clase que administre una agenda. Se debe almacenar para cada 
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú 
con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto, 
Editar contacto, Cerrar agenda.  """

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"Nombre: {self.nombre}, teleféno: {self.telefono}, Email {self.email}"
    
class Agenda:

    def __init__(self):
        self.contactos = []
    
    def añadir_contacto(self, nombre, telefono, email):

        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print(f"Contacto {nombre} añadido correctamente.")
    
    def lista_de_contactos(self):
        if self.contactos:
           for contacto in self.contactos:
                print(contacto)
        else:
            print("No hay contactos en la agenda")

    def buscar_contacto(self, nombre):
        
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(contacto)
                encontrado = True
                return contacto
        
        if not encontrado:
            print(f"No se encontró un contacto con el nombre {nombre}.")
        return None
            
    def editar_contacto(self, nombre):

        contacto = self.buscar_contacto(nombre)
        if contacto:
            nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco para no cambiarlo):")
            nuevo_telefono = input("Introduce el nuevo teléfono (deja en blanco para no cambiarlo): ")
            nuevo_email = input("Introduce el nuevo email (deja en blanco para no cambiarlo): ")

            if nuevo_nombre:
                contacto.nombre = nuevo_nombre
            if nuevo_telefono:
                contacto.telefono = nuevo_telefono
            if nuevo_email:
                contacto.email = nuevo_email
            
            print(f"Contacto {nombre} editado correctamente.")
        else:
            print(f"No se pudo editar el contacto {nombre} por que no exite. ")
    
    def cerrar_agenda(self):
        print("Cerrando la agenda...")
        exit()


def mostrar_menu():
    print("\n---- MENÚ AGENDA ----")
    print("1. Añadir contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")

agenda = Agenda()

while True:
    mostrar_menu()
    opcion = input("Elegi una opción: ")

    if opcion == "1":
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        email = input("Introduce el email del contacto: ")
        agenda.añadir_contacto(nombre, telefono, email)
    
    elif opcion == "2":
        agenda.lista_de_contactos()

    elif opcion == "3":
        nombre = input("Introduce el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)
    
    elif opcion == "4":
        nombre = input("Introduce el nombre del contacto a editar: ")
        agenda.editar_contacto(nombre)

    elif opcion == "5":
        agenda.cerrar_agenda()

    else:
        print("Opción no válida. Intenta de nuevo")
