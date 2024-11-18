from GestionTipoAlimento import GestionTipoAlimento, menu_tipo_alimento
from GestionAlimento import GestionAlimento, menu_alimento
from GestionCombos import GestionCombo, menu_combo
from GestionOrdenes import GestionOrdenes
from Facturacion import Facturacion

class OpcionesAdministrativas:
    def __init__(self, menu_principal):
        #constructor para las clases con las que interactuara el menu
        self.menu_principal = menu_principal
        self.gestion_tipo_alimento = GestionTipoAlimento()
        self.gestion_alimento = GestionAlimento()
        self.gestion_combo = GestionCombo()
        self.gestion_ordenes = GestionOrdenes()
        self.gestion_facturas = Facturacion()
        

    #Muestra las opciones del menu de opciones administrativas
    def mostrar_opciones_administrativas(self):
        print("\n---- Opciones Administrativas ----")
        print("1. Gestion de Tipo de Alimentos")
        print("2. Gestion de Alimentos")
        print("3. Gestion de Combos")
        print("4. Gestion de Ordenes")
        print("5. Facturar")
        print("6. Volver al Menu Principal")
        
        
    def main(self):
        while True:
            #Me muestra las opciones del menu de OpcionesAdministrativas
            self.mostrar_opciones_administrativas()
            opcion = input("Selecciona una opcion: ")
        
#Me permite moverme a las diferentes opciones 'classes' dentro del menu Administrativo
            if opcion == "1":
                print("\n Menu de Tipo de Alimentos...")
                menu_tipo_alimento()
                
            elif opcion == "2":
                print("\n Menu de Alimentos...")
                menu_alimento(self.gestion_alimento)
                
            elif opcion == "3":
                print("\n Menu de Combos...")
                menu_combo(self.gestion_alimento)
                
            elif opcion == "4":
                print("\n Menu de Ordenes...")
                self.gestion_ordenes.menu_ordenes()
                
            elif opcion == "5":
                print("\n Menu Facturacion...")
                self.gestion_facturas.menu_facturacion()
                
            elif opcion == "6":
                print("\n Volviendo al Menu Principal...")
                break
            
            else:
                print("\nOpcion no valida, intenta de nuevo.")