class OpcionesGenerales:
    def __init__(self, menu_principal):
        # Guarda una referencia al menú principal
        self.menu_principal = menu_principal
    
    #Muestra las opciones del menu de opciones generales
    def mostrar_opciones_generales(self):
        print("\n---- Opciones Generales ----")
        print("1. Crear Usuario")
        print("2. Consultar Alimentos")
        print("3. Consulta de puntos e historico de redenciones")
        print("4. Consulta de ordenes")
        print("5. Volver al Menú Principal")
        
    def main(self):
        while True:
            #Muestra las opciones del menu de OpcionesGenerales
            self.mostrar_opciones_generales()
            opcion = input("Selecciona una opcion: ")
                
#Me permite moverme a las diferentes opciones 'classes' dentro del menu General
            if opcion == "1":
                print(" Creando Usuario...")
            elif opcion == "2":
                print(" Consultando Alimentos...")
            elif opcion == "3":
                print(" Consultando de Puntos e Historico de Redenciones...")
            elif opcion == "4":
                print(" Consultando de Ordenes...")
            elif opcion == "5":
                print(" Volviendo al Menu Principal...")
                self.menu_principal.main()
                return
            else:
                print("Opcion no valida, intenta de nuevo!")
                    