import shelve
from datetime import datetime
from CrearUsuario import CrearUsuario
from Facturacion import Facturacion

class ConsultaHistoricoPts(CrearUsuario, Facturacion):
    def __init__(self):
        #inicializa CrearUsuario y Facturacion para acceder a las bases de datos
        CrearUsuario.__init__(self)
        Facturacion.__init__(self)

        #define los nombres de las bases de datos
        self.puntos_db_name = 'puntos.db'
        self.redenciones_db_name = 'redenciones.db'

    def consultar_historial_puntos(self):
        #solicita el nombre del usuario para consultar puntos
        usuario = input("Ingrese el nombre de usuario para consultar el historial de puntos: ")
        
        #verifica si el usuario existe
        if not self.verificar_usuario(usuario):
            print(f"El usuario '{usuario}' no existe en el sistema.")
            return
        
        #obtiene los puntos actuales del usuario
        puntos_totales = self.obtener_puntos_usuario(usuario)
        #calcula el equivalente de puntos totales y su equivalente en dinero
        equivalente_dinero = puntos_totales * 4.75
        #muestra el resumen de puntos totales y su equivalente en ₡₡
        print(f"\n--- Historial de Puntos para el Usuario '{usuario}' ---")
        print(f"Puntos Totales: {puntos_totales} pts")
        print(f"Equivalente en Dinero: ₡{equivalente_dinero:.2f}")

        #inicia la consulta del detalle de redenciones realizadas por el usuario
        print("\nDetalle de Redenciones:")
        with shelve.open(self.redenciones_db_name) as db_redenciones:
            #flag para verificar si se encontraron redenciones
            redenciones_encontradas = False
            #itera sobre las redenciones en la base de datos
            for id_factura, redencion in db_redenciones.items():
                #si la redencion pertenece al usuario consultado, muestra los detalles
                if redencion["usuario"] == usuario:
                    redenciones_encontradas = True
                    #obtiene la fecha y formato para mostrar
                    fecha = redencion["fecha"].strftime('%Y-%m-%d %H:%M:%S')
                    puntos_redimidos = redencion["puntos_redimidos"]
                    #muestra el detalle de cada redencion con el siguiente formato
                    print(f"- Fecha: {fecha}, ID Factura: {id_factura}, Puntos Redimidos: {puntos_redimidos}")
            
            #si no se encontraron redenciones, muestra el siguiente mensaje
            if not redenciones_encontradas:
                print("No se encontraron redenciones para este usuario.")

    def menu_consulta_historial(self):
        #loop del menu de consulta de historial de puntos
        while True:
            print("\n--- Menu de Consulta de Historial de Puntos ---")
            print("1. Consultar historial de puntos de un usuario")
            print("2. Volver al Menu General")
            
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                self.consultar_historial_puntos()
            elif opcion == "2":
                print("Volviendo al Menu General...")
                break
            else:
                print("Opción no valida, intente de nuevo.")

# Ejemplo de uso del menú
if __name__ == "__main__":
    consulta_historial = ConsultaHistoricoPts()
    consulta_historial.menu_consulta_historial()