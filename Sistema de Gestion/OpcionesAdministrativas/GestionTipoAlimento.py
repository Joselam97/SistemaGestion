import shelve

class GestionTipoAlimento:
    #db_name es la variable que alamacena el nombre del archivo en la base de datos
    def __init__(self, db_name='tipos_alimentos.db'):
        self.db_name = db_name

#Funcion para incluir tipo
    def incluir_tipo(self, descripcion, origen, libre_gluten):
        with shelve.open(self.db_name) as db:
            #Verifica si ya esta incluido en shelve
            if descripcion in db:
                print(f"\nError: Ya existe un tipo de alimento con la descripción '{descripcion}'.")
                return
            #En caso contrario, se agrega el nuevo tipo
            db[descripcion] = {
                'origen': origen,
                'libre_gluten': libre_gluten
            }
            print(f"\nTipo de alimento '{descripcion}' agregado con éxito.")

#Elimina tipo de alimento
    def eliminar_tipo(self, descripcion):
        with shelve.open(self.db_name) as db:
            #En caso de no estar el tipo de alimento en shelve
            if descripcion not in db:
                print(f"\nError: El tipo de alimento '{descripcion}' no existe.")
                return
            #En caso de estar el tipo de la descripcion a otro alimento
            if self.alimento_asociado(descripcion):
                print(f"\nError: No se puede eliminar el tipo '{descripcion}' porque está asociado a alimentos.")
                return
            #Si se encuentra en shelve y no esta asociado a alimentos se puede eliminar
            del db[descripcion]
            print(f"\nTipo de alimento '{descripcion}' eliminado con éxito.")

#Funcion para modificar tipo de alimento
    def modificar_tipo(self, descripcion, nuevo_origen=None, nuevo_libre_gluten=None):
        with shelve.open(self.db_name) as db:
            #Verifica si extiste
            if descripcion not in db:
                print(f"\nError: El tipo de alimento '{descripcion}' no existe.")
                return
            tipo_alimento = db[descripcion]
            #Si la descripcion del origen existe se modifica
            if nuevo_origen is not None:
                tipo_alimento['origen'] = nuevo_origen
            #Si la descripcion del gluten existe se modifica
            if nuevo_libre_gluten is not None:
                tipo_alimento['libre_gluten'] = nuevo_libre_gluten
            #se agrega a la base de datos
            db[descripcion] = tipo_alimento
            print(f"\nTipo de alimento '{descripcion}' modificado con éxito.")

#muestra lo que hay registrado
    def mostrar_tipos(self):
        with shelve.open(self.db_name) as db:
            #en caso de no haber nada
            if not db:
                print("\nNo hay tipos de alimentos registrados.")
            #en caso de haber registro se sigue este proceso
            else:
                print("\nTipos de alimentos registrados:")
                for descripcion, datos in db.items():
                    origen = datos['origen']
                    libre_gluten = 'Sí' if datos['libre_gluten'] else 'No'
                    print(f"- {descripcion}: Origen: {origen}, Libre de gluten: {libre_gluten}")

    def alimento_asociado(self, descripcion):
        return False

#funcion para mostrar el menu de GestionTipoAlimento
def menu_tipo_alimento():
    gestion = GestionTipoAlimento()

    while True:
        print("\n--- Menú de Gestión de Tipos de Alimentos ---")
        print("1. Incluir tipo de alimento")
        print("2. Eliminar tipo de alimento")
        print("3. Modificar tipo de alimento")
        print("4. Mostrar tipos de alimentos")
        print("5. Volver al Menu Administrativo")
        
        opcion = input("Elija una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción: ")
            origen = input("Ingrese el origen: ")
            libre_gluten = input("¿Es libre de gluten? (sí/no): ").lower() == 'sí'
            gestion.incluir_tipo(descripcion, origen, libre_gluten)

        elif opcion == "2":
            descripcion = input("Ingrese la descripción del tipo de alimento a eliminar: ")
            gestion.eliminar_tipo(descripcion)

        elif opcion == "3":
            descripcion = input("Ingrese la descripción del tipo de alimento a modificar: ")
            nuevo_origen = input("Ingrese el nuevo origen (dejar en blanco si no desea cambiar): ") or None
            libre_gluten_input = input("¿Es libre de gluten? (si/no, deje en blanco si no desea cambiar): ")
            nuevo_libre_gluten = None if libre_gluten_input == '' else libre_gluten_input.lower() == 'sí'
            gestion.modificar_tipo(descripcion, nuevo_origen, nuevo_libre_gluten)

        elif opcion == "4":
            gestion.mostrar_tipos()

        elif opcion == "5":
            print("Volviendo al Menu Administrativo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Iniciar el menú
menu_tipo_alimento()

