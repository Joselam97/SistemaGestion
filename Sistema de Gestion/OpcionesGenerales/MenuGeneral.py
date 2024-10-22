class OpcionesGenerales:
    
    #Muestra las opciones del menu de opciones generales
    def mostrar_opciones_generales(self):
        print("---- Opciones Generales ----")
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
                print("1. Crear Usuario")
            elif opcion == "2":
                print("2. Consultar Alimentos")
            elif opcion == "3":
                print("3. Consulta de Puntos e Historico de Redenciones")
            elif opcion == "4":
                print("4. Consulta de Ordenes")
            elif opcion == "5":
                print("Volviendo al Menu Principal...")
                break
            else:
                print("Opcion no valida, intenta de nuevo!")
                    
if __name__ == "__main__":
    menuGeneral = OpcionesGenerales()
    menuGeneral.main()