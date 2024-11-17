from CrearUsuario import CrearUsuario
from ConsultaAlimentos import ConsultaAlimento
from GestionAlimento import GestionAlimento
from GestionCombos import GestionCombo
from GestionTipoAlimento import GestionTipoAlimento
from ConsultaHistoricoPts import ConsultaHistoricoPts
from ConsultaOrdenes import ConsultaOrdenes

class OpcionesGenerales:
    def __init__(self, menu_principal):
        #constructor para las clases con las que interactuara el menu
        self.menu_principal = menu_principal
        self.crear_usuario = CrearUsuario()
        self.consulta_alimento = ConsultaAlimento(
            gestion_alimento=GestionAlimento(),
            gestion_combo=GestionCombo(),
            gestion_tipo=GestionTipoAlimento()
        )
        self.consulta_historico_pts = ConsultaHistoricoPts()
        self.consulta_ordenes = ConsultaOrdenes()
    
    
    #Muestra las opciones del menu de opciones generales
    def mostrar_opciones_generales(self):
        print("\n---- Opciones Generales ----")
        print("1. Crear Usuario")
        print("2. Consultar Alimentos")
        print("3. Consulta de puntos e historico de redenciones")
        print("4. Consulta de ordenes")
        print("5. Volver al Menu Principal")
        
        
    def main(self):
        while True:
            #Muestra las opciones del menu de OpcionesGenerales
            self.mostrar_opciones_generales()
            opcion = input("Selecciona una opcion: ")
                
#Me permite moverme a las diferentes opciones 'classes' dentro del menu General
            if opcion == "1":
                print("\n Creacion Usuario...")
                self.crear_usuario.menu_usuarios()
                
            elif opcion == "2":
                print("\n Consultando Alimentos...")
                self.consulta_alimento.menu_consulta_alimentos()
                
            elif opcion == "3":
                print("\n Consultando de Puntos e Historico de Redenciones...")
                self.consulta_historico_pts.menu_consulta_historial()
                
            elif opcion == "4":
                print("\n Consultando de Ordenes...")
                self.consulta_ordenes.menu_consulta_ordenes()
                
            elif opcion == "5":
                print("\n Volviendo al Menu Principal...")
                break
            
            else:
                print("\n Opcion no valida, intenta de nuevo!")
                    