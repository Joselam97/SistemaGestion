import shelve
from GestionAlimento import GestionAlimento
from GestionCombos import GestionCombo
from GestionTipoAlimento import GestionTipoAlimento

class ConsultaAlimento:
    def __init__(self, gestion_alimento: GestionAlimento, gestion_combo: GestionCombo, gestion_tipo: GestionTipoAlimento):
        self.gestion_alimento = gestion_alimento
        self.gestion_combo = gestion_combo
        self.gestion_tipo = gestion_tipo

    def mostrar_alimentos(self):
        print("\nLista de Alimentos:")
        self.gestion_alimento.mostrar_alimentos()

    def mostrar_combos(self):
        print("\nLista de Combos:")
        self.gestion_combo.mostrar_combos()  # Asegúrate de que este método esté implementado en GestionCombo

    def mostrar_tipos_alimentos(self):
        print("\nLista de Tipos de Alimentos:")
        
        # Abrimos la base de datos de tipos de alimentos y mostramos todos los tipos
        with shelve.open(self.gestion_tipo.db_name) as db_tipos:
            if db_tipos:
                for descripcion, info in db_tipos.items():
                    print(f"- {descripcion}: Origen: {info['origen']}, Libre de gluten: {'Sí' if info['libre_gluten'] else 'No'}")
            else:
                print("No hay tipos de alimentos disponibles.")

    def menu_consulta_alimentos(self):
        gestion_alimento = GestionAlimento()
        gestion_tipo_alimento = GestionTipoAlimento()
        
        while True:
            print("\n--- Menú de Consulta de Alimentos y Combos ---")
            print("1. Mostrar todos los alimentos")
            print("2. Mostrar todos los combos")
            print("3. Mostrar todos los tipos de alimentos")
            print("4. Volver al Menu General")

            opcion = input("Elija una opción: ")

            if opcion == '1':
                self.mostrar_alimentos()
            elif opcion == '2':
                self.mostrar_combos()
            elif opcion == '3':
                self.mostrar_tipos_alimentos()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, por favor selecciona nuevamente.")

# Ejemplo de uso:
if __name__ == "__main__":
    gestion_alimento = GestionAlimento()  # Asegúrate de que la clase GestionAlimento esté correctamente implementada
    gestion_combo = GestionCombo(gestion_alimento=gestion_alimento)  # Asegúrate de que la clase GestionCombo esté correctamente implementada
    gestion_tipo = GestionTipoAlimento()  # Instanciamos GestionTipoAlimento
    consulta_alimento = ConsultaAlimento(gestion_alimento, gestion_combo, gestion_tipo)

    consulta_alimento.menu_consulta_alimentos()

