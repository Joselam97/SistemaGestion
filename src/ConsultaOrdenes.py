import shelve
from GestionOrdenes import GestionOrdenes

class ConsultaOrdenes(GestionOrdenes):
    def __init__(self):
        super().__init__()
    
    def consultar_ordenes_usuario(self):
        usuario = self.solicitar_usuario()
        if usuario is None:
            return

        ordenes = []
        
        # Abrir la base de datos de órdenes y mostrar las órdenes del usuario
        with shelve.open(self.ordenes_db_name) as db_ordenes:
            if usuario in db_ordenes:
                print(f"\n--- Órdenes del usuario '{usuario}' ---")
                for id_orden, datos in db_ordenes[usuario].items():
                    ordenes.append(id_orden)
                    print(f"ID Orden: {id_orden}, Fecha y Hora: {datos['fecha_hora']}")

                if not ordenes:
                    print("No se encontraron órdenes para este usuario.")
                    return
            else:
                print("No se encontraron órdenes para este usuario.")
                return

        # Permitir seleccionar una orden y ver los detalles
        while True:
            id_orden = input("\nIngrese el identificador de la orden para ver el detalle (o escriba 'volver' para regresar): ")
            if id_orden.lower() == "volver":
                break
            elif id_orden in ordenes:
                self.ver_detalle_orden(usuario, id_orden)
            else:
                print("Identificador de orden no válido. Intente de nuevo.")
    
    def ver_detalle_orden(self, usuario, id_orden):
        # Abrir la base de datos y mostrar el detalle de la orden seleccionada
        with shelve.open(self.ordenes_db_name) as db_ordenes:
            if usuario in db_ordenes and id_orden in db_ordenes[usuario]:
                datos = db_ordenes[usuario][id_orden]
                print(f"\n--- Detalle de la Orden '{id_orden}' ---")
                print(f"Usuario: {usuario}")
                print(f"Fecha y Hora: {datos['fecha_hora']}")
                print("Combos:")
                for combo, cantidad in datos["combos"].items():
                    print(f" - {combo}: {cantidad}")
                print("Alimentos:")
                for alimento, cantidad in datos["alimentos"].items():
                    print(f" - {alimento}: {cantidad}")
                print(f"Facturada: {'Sí' if datos['facturada'] else 'No'}")
                print("\n--- Fin del Detalle ---")
            else:
                print("La orden no existe o no está asociada con este usuario.")

    def menu_consulta_ordenes(self):
        while True:
            print("\n--- Menú de Consulta de Órdenes ---")
            print("1. Consultar órdenes de un usuario")
            print("2. Volver al Menu General")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.consultar_ordenes_usuario()
            elif opcion == "2":
                print("Volviendo al Menu General...")
                break
            else:
                print("Opcion no válida. Intente de nuevo.")

# Ejemplo de uso
if __name__ == "__main__":
    consulta_ordenes = ConsultaOrdenes()
    consulta_ordenes.menu_consulta_ordenes()
