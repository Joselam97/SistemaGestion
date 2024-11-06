import shelve

class GestionTipoAlimento:
    #db_name es la variable que alamacena el nombre del archivo en la base de datos
    def __init__(self, db_name='tipos_alimentos.db'):
        self.db_name = db_name
        
    def existe_tipo(self, tipo):
        with shelve.open(self.db_name) as db:
            return tipo in db


#Funcion para incluir tipo
    def incluir_tipo(self, descripcion, origen, libre_gluten):
        #con shelve se abre el archivo de la base de datos db_alimentos para hacer la consulta
        with shelve.open(self.db_name) as db:
            
            #Verifica si ya esta incluido en shelve
            if descripcion in db:
                print(f"\nError: Ya existe un tipo de alimento con la descripción '{descripcion}'.")
                return
            
            #En caso contrario, se agrega el nuevo tipo, se pide el origen y si contiene gluten
            db[descripcion] = {
                'origen': origen,
                'libre_gluten': libre_gluten
            }
            print(f"\nTipo de alimento '{descripcion}' agregado con éxito.")

#Elimina tipo de alimento
    def eliminar_tipo(self, descripcion):
        #con shelve se abre el archivo de la base de datos db_alimentos para hacer la consulta
        with shelve.open(self.db_name) as db:
            
            #En caso de no estar el tipo de alimento en shelve
            if descripcion not in db:
                print(f"\nError: El tipo de alimento '{descripcion}' no existe.")
                return
            #En caso de estar el tipo de la descripcion en otro alimento
            if self.alimento_asociado(descripcion):
                print(f"\nError: No se puede eliminar el tipo '{descripcion}' porque está asociado a alimentos.")
                return
            #Si se encuentra en shelve y no esta asociado a alimentos se puede eliminar
            del db[descripcion]
            print(f"\nTipo de alimento '{descripcion}' eliminado con éxito.")

#Funcion para modificar tipo de alimento
    def modificar_tipo(self, descripcion, nuevo_origen=None, nuevo_libre_gluten=None):
        #con shelve se abre el archivo de la base de datos db_alimentos para hacer la consulta
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
        #con shelve se abre el archivo de la base de datos db_alimentos para hacer la consulta
        with shelve.open(self.db_name) as db:
            
            #en caso de no haber nada
            if not db:
                print("\nNo hay tipos de alimentos registrados.")
            #en caso de haber registro se sigue este proceso
            else:
                print("\nTipos de alimentos registrados:")
                #itera por los datos que tiene en la base de datos
                for descripcion, datos in db.items():
                    origen = datos['origen']
                    libre_gluten = 'si' if datos['libre_gluten'] else 'no'
                    #imprime cada iteracion de datos guardados de tipo de alimento
                    print(f"- {descripcion}: Origen: {origen}, Libre de gluten: {libre_gluten}")


    #funcion para filtrar por origen en ConsultaAlimentos
    def filtrar_por_origen(self, origen_filtro):
        with shelve.open(self.db_name) as db:
            print(f"\nTipos de alimentos con origen '{origen_filtro}':")
            encontrados = False
            for descripcion, datos in db.items():
                if datos['origen'].lower() == origen_filtro.lower():
                    libre_gluten = 'sí' if datos['libre_gluten'] else 'no'
                    print(f"- {descripcion}: Libre de gluten: {libre_gluten}")
                    encontrados = True
            if not encontrados:
                print(f"No se encontraron alimentos de origen '{origen_filtro}'.")
                

    def alimento_asociado(self, descripcion): #verifica si el tipo de alimento esta asociado a algun alimento
        with shelve.open('alimentos.db') as db_alimentos:
            for alimento in db_alimentos.values():
                if alimento['tipo'] == descripcion:
                    return True
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
        
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripcion: ")
            origen = input("Ingrese el origen: ")
            libre_gluten = input("¿Es libre de gluten? (si/no): ").lower() == 'si'
            gestion.incluir_tipo(descripcion, origen, libre_gluten)

        elif opcion == "2":
            print("\n --- Tipos de alimentos registrados --- ")
            gestion.mostrar_tipos()
            descripcion = input("\nIngrese la descripción del tipo de alimento a eliminar: ")
            gestion.eliminar_tipo(descripcion)

        elif opcion == "3":
            print("\n --- Tipos de alimentos registrados --- ")
            gestion.mostrar_tipos()
            descripcion = input("\nIngrese la descripción del tipo de alimento a modificar: ")
            nuevo_origen = input("Ingrese el nuevo origen (dejar en blanco si no desea cambiar): ") or None
            libre_gluten_input = input("¿Es libre de gluten? (si/no, deje en blanco si no desea cambiar): ")
            nuevo_libre_gluten = None if libre_gluten_input == 'no' else libre_gluten_input.lower() == 'si'
            gestion.modificar_tipo(descripcion, nuevo_origen, nuevo_libre_gluten)

        elif opcion == "4":
            gestion.mostrar_tipos()

        elif opcion == "5":
            print("Volviendo al Menu Administrativo...")
            break

        else:
            print("Opción no valida, intente de nuevo.")

if __name__ == "__main__":
    menu_tipo_alimento()
