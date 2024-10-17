class MenuPrincipal:
    #Muestra las opciones del menu principal
    def mostrar_menu_principal(self):
        print("Bienvenido al sistema de gestión del restaurante")
        print("1. Opciones Administrativas")
        print("2. Opciones Generales")
        print("3. Salir")

#Muestra las opciones del menu Administrativo
    def opciones_administrativas(self):
        print("---- Opciones Administrativas ----")
        print("1. Gestion de Tipo de Alimentos")
        print("2. Gestion de Alimentos")
        print("3. Gestion de Combos")
        print("4. Gestion de Ordenes")
        print("5. Facturar")
        print("6. Reporte de Ventas")
        print("7. Volver al Menú Principal")

#Muestra las opciones del Menu General
    def opciones_generales(self):
        print("---- Opciones Generales ----")
        print("1. Crear Usuario")
        print("2. Consultar Alimentos")
        print("3. Consulta de puntos e historico de redenciones")
        print("3. Consulta de ordenes")
        print("4. Volver al Menú Principal")

#Solicita la opcion que queramos escoger para desplegar sus opciones
    def main(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Selecciona una opción: ")
        
            if opcion == "1":
                self.opciones_administrativas()
            elif opcion == "2":
                self.opciones_generales()
            elif opcion == "3":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.main()
