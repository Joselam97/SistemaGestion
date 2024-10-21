
class MenuPrincipal:
    #Muestra las opciones del menu principal
    def mostrar_menu_principal(self):
        print("Bienvenido al sistema de gestión del restaurante")
        print("1. Opciones Administrativas")
        print("2. Opciones Generales")
        print("3. Salir")


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
            
            #Supongo que aca incerto las funciones para moverme a las diferentes clases
            if opcion == "1":
                print("1. Opciones Administrativas")
            elif opcion == "2":
                print("2. Opciones Generales")
            elif opcion == "3":
                print("3. Saliendo del sistema...")
                break
            else:
                print("4. Indique una opcion valida!")


if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.main()
