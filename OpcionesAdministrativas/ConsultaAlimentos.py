import shelve
from GestionAlimento import GestionAlimento
from GestionCombos import GestionCombo
from GestionTipoAlimento import GestionTipoAlimento

class ConsultaAlimento:
    def __init__(self, gestion_alimento: GestionAlimento, gestion_combo: GestionCombo, gestion_tipo: GestionTipoAlimento):
        self.gestion_alimento = gestion_alimento
        self.gestion_combo = gestion_combo
        self.gestion_tipo = gestion_tipo

    #muestra los alimentos de GestionAlimento
    def mostrar_alimentos(self):
        print("\nLista de Alimentos:")
        self.gestion_alimento.mostrar_alimentos()
    
    #muestra los combos de GestionCombos
    def mostrar_combos(self):
        print("\nLista de Combos:")
        self.gestion_combo.mostrar_combos()  
    
    #muestra los tipos de alimentos de GestionTipoAlimento, incluyendo un metodo para filtrarlos por origen
    def mostrar_tipos_alimentos(self, filtrar=False):
        print("\nLista de Tipos de Alimentos:")
        
        #abre la base de dato de shelve que contiene los tipos de alimentos gracias a 'db_tipos'
        with shelve.open(self.gestion_tipo.db_name) as db_tipos:
            if not db_tipos:
                print("No hay tipos de alimentos disponibles.")
                return
            
            #si se filtra se muestran los tipos de alimentos con respecto a su origen
            if filtrar:
                origen_filtro = input("Ingrese el origen a filtrar (por ejemplo: 'vegetal' o 'animal'): ").lower()
                encontrados = False
                #en caso de encontrarse el origen por el cual filtre
                for descripcion, info in db_tipos.items():
                    #si la palabra ingresada con la variable 'origen_filtro' en case insensitive se encuentra, entonces imprime el tipo
                    if info['origen'].lower() == origen_filtro:
                        print(f"- {descripcion}: Origen: {info['origen']}, Libre de gluten: {'Sí' if info['libre_gluten'] else 'No'}")
                        #transforma la variable booleana a True
                        encontrados = True
                if not encontrados:
                    print(f"No se encuentra ningún alimento de origen '{origen_filtro}'.")
            #si no se filtra, se muestran todos los tipos de alimentos
            else:
                for descripcion, info in db_tipos.items():
                    print(f"- {descripcion}: Origen: {info['origen']}, Libre de gluten: {'Si' if info['libre_gluten'] else 'No'}")

    def menu_consulta_alimentos(self):
        gestion_alimento = GestionAlimento()
        gestion_tipo_alimento = GestionTipoAlimento()
        
        while True:
            print("\n--- Menú de Consulta de Alimentos y Combos ---")
            print("1. Mostrar todos los alimentos")
            print("2. Mostrar todos los combos")
            print("3. Mostrar todos los tipos de alimentos con filtro por origen")
            print("4. Volver al Menu General")

            opcion = input("Seleccione una opcion: ")

            if opcion == '1':
                self.mostrar_alimentos()
                
            elif opcion == '2':
                self.mostrar_combos()
                
            #usa el metodo filtrar por origen y hereda de la clase GestionTipoAlimento para 'mostrar_tipos_alimentos'    
            elif opcion == '3':
                self.mostrar_tipos_alimentos()
                print("\n --- Tipos de Alimentos Registrados para Filtrar --- \n")
                self.mostrar_tipos_alimentos(filtrar=True)
                
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, por favor selecciona nuevamente.")

#ejmplo para usar y asignacion de variables para cada clase
if __name__ == "__main__":
    gestion_alimento = GestionAlimento()  
    gestion_combo = GestionCombo(gestion_alimento=gestion_alimento)  
    gestion_tipo = GestionTipoAlimento()  
    consulta_alimento = ConsultaAlimento(gestion_alimento, gestion_combo, gestion_tipo)

    consulta_alimento.menu_consulta_alimentos()

