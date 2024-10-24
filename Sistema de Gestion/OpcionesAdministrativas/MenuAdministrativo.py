

class OpcionesAdministrativas:
    #Muestra las opciones del menu de opciones administrativas
    def mostrar_opciones_administrativas(self):
        print("---- Opciones Administrativas ----")
        print("1. Gestion de Tipo de Alimentos")
        print("2. Gestion de Alimentos")
        print("3. Gestion de Combos")
        print("4. Gestion de Ordenes")
        print("5. Facturar")
        print("6. Reporte de Ventas")
        print("7. Volver al Menú Principal")
        
    def main(self):
        while True:
            #Me muestra las opciones del menu de OpcionesAdministrativas
            self.mostrar_opciones_administrativas()
            opcion = input("Selecciona una opción: ")
        
#Me permite moverme a las diferentes opciones 'classes' dentro del menu Administrativo
            if opcion == "1":
                print("1. Gestion de Tipo de Alimentos")
            elif opcion == "2":
                print("2. Gestion de Alimentos")
            elif opcion == "3":
                print("3. Gestion de Combos")
            elif opcion == "4":
                print("4. Gestion de Ordenes")
            elif opcion == "5":
                print("5. Facturar")
            elif opcion == "6":
                print("6. Reporte de Ventas")
            elif opcion == "7":
                print("Volviendo al Menu Principal...")
                #El break sera solo mientras no he asociado los menus
                break
            else:
                print("Opcion no válida, intenta de nuevo.")
            
            
if __name__ == "__main__":
    menuAdministrativo = OpcionesAdministrativas()
    menuAdministrativo.main()