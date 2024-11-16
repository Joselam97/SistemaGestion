import shelve
from GestionOrdenes import GestionOrdenes

class ConsultaOrdenes(GestionOrdenes):
    def __init__(self):
        #inicializa la base GestionOrdenes para acceder a sus metodos y atributos
        super().__init__()
    
    def consultar_ordenes_usuario(self):
        #solicita el nombre del usuario cuyas ordenes se desean consultar
        usuario = self.solicitar_usuario()
        #si el usuario decide regresar al menu anterior se termina este metodo
        if usuario is None:
            return

#lista para almacenar los identificadores de las ordenes del usuario
        ordenes = []
        
        #abre la base de datos de órdenes y mostrar las ordenes del usuario
        with shelve.open(self.ordenes_db_name) as db_ordenes:
            if usuario in db_ordenes:
                print(f"\n--- Órdenes del usuario '{usuario}' ---")
                #itera sobre cada orden del usuario, muestra el Id, fecha y hora
                for id_orden, datos in db_ordenes[usuario].items():
                    ordenes.append(id_orden)
                    print(f"ID Orden: {id_orden}, Fecha y Hora: {datos['fecha_hora']}")

#si no se encontraron ordenes, muestra un mensaje y termina el metodo
                if not ordenes:
                    print("No se encontraron órdenes para este usuario.")
                    return
            else:
                #muestra un mensaje si el usuario no tiene ordenes
                print("No se encontraron órdenes para este usuario.")
                return

        #bucle para permitir al usuario seleccionar una orden especifica y ver sus detalles
        while True:
            id_orden = input("\nIngrese el identificador de la orden para ver el detalle (o escriba 'volver' para regresar): ")
            if id_orden.lower() == "volver":
                break
            #si el ID de la orden es invalido
            elif id_orden in ordenes:
                self.ver_detalle_orden(usuario, id_orden)
            else:
                print("Identificador de orden no valido. Intente de nuevo.")
    
    def ver_detalle_orden(self, usuario, id_orden):
        #abre la base de datos y mostrar el detalle de la orden seleccionada
        with shelve.open(self.ordenes_db_name) as db_ordenes:
            #verifica que el usuario y el id de la orden existen en la Base de datos
            if usuario in db_ordenes and id_orden in db_ordenes[usuario]:
                datos = db_ordenes[usuario][id_orden]
                #muestra el detalle de la orden con el siguiente formato
                print(f"\n--- Detalle de la Orden '{id_orden}' ---")
                print(f"Usuario: {usuario}")
                print(f"Fecha y Hora: {datos['fecha_hora']}")
                print("Combos:")
                #muestra cada combo en la orden y su cantidad
                for combo, cantidad in datos["combos"].items():
                    print(f" - {combo}: {cantidad}")
                print("Alimentos:")
                #muestra cada alimento en la orden y su cantidad
                for alimento, cantidad in datos["alimentos"].items():
                    print(f" - {alimento}: {cantidad}")
                    #indica si la orden fue facturada o no
                print(f"Facturada: {'Si' if datos['facturada'] else 'No'}")
                print("\n--- Fin del Detalle ---")
            else:
                #muestra un mensaje si la orden no existe o no esta asociada al usuario
                print("La orden no existe o no esta asociada con este usuario.")

    def menu_consulta_ordenes(self):
        #loop principal del menu de consulta de ordenes
        while True:
            print("\n--- Menu de Consulta de Ordenes ---")
            print("1. Consultar ordenes de un usuario")
            print("2. Volver al Menu General")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.consultar_ordenes_usuario()
            elif opcion == "2":
                print("Volviendo al Menu General...")
                break
            else:
                print("Opcion no valida. Intente de nuevo.")

#ejemplo de uso
if __name__ == "__main__":
    #crea una instancia de ConsultaOrdenes y muestra el menu de consulta de ordenes
    consulta_ordenes = ConsultaOrdenes()
    consulta_ordenes.menu_consulta_ordenes()
