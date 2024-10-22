#Importo shelve para alamacenar los datos
import shelve

class GestionTipoAlimento:
    def __init__(self, db_name='tipos_alimentos.db'):
        #Aca guardo los tipos de alimentos
        self.db_name = db_name

#Funcion que va a describir el tipo de alimento
    def incluir_tipo(self, descripcion, origen, libre_gluten):
        with shelve.open(self.db_name) as db:
            
            if descripcion in db:
                print(f"\nError: Ya existe un tipo de alimento con la descripción '{descripcion}'.")
                return

            #Agrego el tipo de alimento
            db[descripcion] = {
                'origen': origen,
                'libre_gluten': libre_gluten
            }
            print(f"\nTipo de alimento '{descripcion}' agregado con éxito.")


#Funcion para saber si el tipo de alimento existe
    def eliminar_tipo(self, descripcion):
        with shelve.open(self.db_name) as db:
            if descripcion not in db:
                print(f"\nError: El tipo de alimento '{descripcion}' no existe.")
                return

#Funcion para saber si la descripcion esta asociada a algun alimento
            if self.alimento_asociado(descripcion):
                print(f"\nError: No se puede eliminar el tipo '{descripcion}' porque está asociado a alimentos.")
                return

#Elimina el tipo de alimento
            del db[descripcion]
            print(f"\nTipo de alimento '{descripcion}' eliminado con éxito.")
            

    def modificar_tipo(self, descripcion, nuevo_origen=None, nuevo_libre_gluten=None):
        with shelve.open(self.db_name) as db:
            #Identifico si el tipo de alimento existe
            if descripcion not in db:
                print(f"\nError: El tipo de alimento '{descripcion}' no existe.")
                return

            #Modifica valores
            tipo_alimento = db[descripcion]
            if nuevo_origen is not None:
                tipo_alimento['origen'] = nuevo_origen
            if nuevo_libre_gluten is not None:
                tipo_alimento['libre_gluten'] = nuevo_libre_gluten
            db[descripcion] = tipo_alimento
            print(f"\nTipo de alimento '{descripcion}' modificado con éxito.")

    def mostrar_tipos(self):
        with shelve.open(self.db_name) as db:
            if not db:
                print("\nNo hay tipos de alimentos registrados.")
            else:
                print("\nTipos de alimentos registrados:")
                for descripcion, datos in db.items():
                    origen = datos['origen']
                    libre_gluten = 'Sí' if datos['libre_gluten'] else 'No'
                    print(f"- {descripcion}: Origen: {origen}, Libre de gluten: {libre_gluten}")

    def alimento_asociado(self, descripcion):
        # Simular que no hay alimentos asociados para este ejemplo
        # En un proyecto real, deberías verificar si este tipo de alimento está asociado a algún alimento
        return False

#Ejemplo de uso
gestion = GestionTipoAlimento()

#Ingreso de alimentos
gestion.incluir_tipo("Fruta", "Vegetal", True)
gestion.incluir_tipo("Cereal", "Vegetal", False)
gestion.incluir_tipo("Arroz", "Vegetal", False)

#Muestra lo que tengo
gestion.mostrar_tipos()

#Modifica algun tipo, por ejemplo el cereal lo vuelve libre de gluten
gestion.modificar_tipo("Cereal", nuevo_libre_gluten=True)

#Intentar eliminar un tipo que no existe, para recibir el error
gestion.eliminar_tipo("Carne")

#Elimino un alimento existente
gestion.eliminar_tipo("Fruta")

#Vuelvo a mostrar lo que tengo
gestion.mostrar_tipos()
