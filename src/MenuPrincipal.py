from MenuAdministrativo import OpcionesAdministrativas
from MenuGeneral import OpcionesGenerales

class MenuPrincipal:
    #inicializa los submenus
    def __init__(self):
        self.menu_generales = OpcionesGenerales(self)
        self.menu_administrativas = OpcionesAdministrativas(self)
    
    
    #Muestra las opciones del menu principal
    def mostrar_menu_principal(self):
        print("\nBienvenido al sistema de gestión del restaurante")
        print("1. Opciones Administrativas")
        print("2. Opciones Generales")
        print("3. Salir")


#Solicita la opcion que queramos escoger para desplegar sus opciones
    def main(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Selecciona una opción: ")
            
            #Supongo que aca incerto las funciones para moverme a las diferentes clases
            if opcion == "1":
                #print("1. Opciones Administrativas")
                self.menu_administrativas.main()
            elif opcion == "2":
                #print("2. Opciones Generales")
                self.menu_generales.main()
            elif opcion == "3":
                print("\n Saliendo del sistema...\n")
                break
            else:
                print("\n Indique una opcion valida!")


if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.main()
