import shelve
#importa la libreria para manejar fechas
from datetime import datetime

class CrearUsuario:
    #crea una variable llamada 'usuarios.db' y la guarda en la base de datos principal
    def __init__(self, db_name='usuarios.db'):
        self.db_name = db_name

    #funcion para crear un nuevo usuario con nombre de usuario, nombre y fecha de nacimiento
    def crear_usuario(self, nombre_usuario, nombre, fecha_nacimiento):
        with shelve.open(self.db_name) as db_usuarios:
            #verifica si el nombre de usuario ya existe
            if nombre_usuario in db_usuarios:
                print(f"Error: El nombre de usuario '{nombre_usuario}' ya existe.")
                return
            
            #verifica si la fecha de nacimiento tiene un formato correcto
            try:
                #convierte la fecha de DD-MM-YYYY a formato de fecha dia-mes-año
                fecha_nacimiento_obj = datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
                #en caso de brindar la fecha con un mal formato
            except ValueError:
                print("Error: El formato de la fecha de nacimiento debe ser 'DD-MM-YYYY'.")
                return

            #diccionario para guardar datos de usuarios
            db_usuarios[nombre_usuario] = {
                'nombre': nombre,
                'fecha_nacimiento': fecha_nacimiento_obj.strftime('%d-%m-%Y'),  # Guardar en el formato correcto
                'puntos': 10  #siempre se asignan 10pts por usuario
            }
            print(f"Usuario '{nombre_usuario}' creado con éxito. Se han asignado 10 puntos.")

    #funcion para mostrar usuarios guardados
    def mostrar_usuarios(self):
        with shelve.open(self.db_name) as db_usuarios:
            #en caso de aun no haber usuarios
            if not db_usuarios:
                print("No hay usuarios registrados.")
            #en caso de haber usuarios, imprime los items del diccionario anteriormente creado
            else:
                print("\nUsuarios registrados:")
                for nombre_usuario, datos in db_usuarios.items():
                    print(f"- Usuario: {nombre_usuario}, Nombre: {datos['nombre']}, "
                          f"Fecha de nacimiento: {datos['fecha_nacimiento']}, Puntos: {datos['puntos']}")
                    
    #funcion para eliminar usuarios
    def eliminar_usuario(self, nombre_usuario):
        with shelve.open(self.db_name, writeback=True) as db_usuarios:
            #en caso de existir el usuario, se solicita nombre de usuario para eliminarlo de 'db_name'
            if nombre_usuario in db_usuarios:
                del db_usuarios[nombre_usuario]
                print(f"Usuario '{nombre_usuario}' eliminado con éxito.")
            else:
                print(f"Error: El usuario '{nombre_usuario}' no existe en el sistema.")

#ejemplo de uso del menu 
if __name__ == "__main__":
    gestion_usuarios = CrearUsuario()

    while True:
        print("\n--- Menú de Creación de Usuarios ---")
        print("1. Crear nuevo usuario")
        print("2. Mostrar usuarios")
        print("3. Eliminar usuarios")
        print("4. Volver al Menu General")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #implementa un bucle para regresar en caso de se escriba 'volver'
            while True:
                nombre_usuario = input("Ingrese el nombre de usuario (o 'volver'): ")
                if nombre_usuario.lower() == 'volver':
                   break
                nombre = input("Ingrese el nombre: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento (formato DD-MM-YYYY): ")

                gestion_usuarios.crear_usuario(nombre_usuario, nombre, fecha_nacimiento)

        elif opcion == "2":
            gestion_usuarios.mostrar_usuarios()
            
            
        elif opcion == "3":
            #implementa un bucle para regresar en caso de se escriba 'volver'
            while True:
                gestion_usuarios.mostrar_usuarios()
                print("\n --- Usuarios a eliminar --- \n")
                nombre_usuario = input("Ingrese el nombre de usuario a eliminar (o 'volver'): ")
                if nombre_usuario.lower() == 'volver':
                    break
                gestion_usuarios.eliminar_usuario(nombre_usuario)

        elif opcion == "4":
            print("Volviendo al Menu General...")
            break

        else:
            print("Opción no válida, intente de nuevo.")
