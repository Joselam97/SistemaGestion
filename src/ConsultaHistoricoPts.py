import shelve
from datetime import datetime
from CrearUsuario import CrearUsuario
from Facturacion import Facturacion

class ConsultaHistoricoPts(CrearUsuario, Facturacion):
    def __init__(self):
        # Inicializa CrearUsuario y Facturacion para acceder a las bases de datos
        CrearUsuario.__init__(self)
        Facturacion.__init__(self)

        # Define los nombres de las bases de datos
        self.puntos_db_name = 'puntos.db'
        self.redenciones_db_name = 'redenciones.db'

    def consultar_historial_puntos(self):
        usuario = input("Ingrese el nombre de usuario para consultar el historial de puntos: ")
        
        # Verificar si el usuario existe
        if not self.verificar_usuario(usuario):
            print(f"El usuario '{usuario}' no existe en el sistema.")
            return
        
        # Obtener los puntos actuales del usuario
        puntos_totales = self.obtener_puntos_usuario(usuario)
        equivalente_dinero = puntos_totales * 4.75
        print(f"\n--- Historial de Puntos para el Usuario '{usuario}' ---")
        print(f"Puntos Totales: {puntos_totales} pts")
        print(f"Equivalente en Dinero: ₡{equivalente_dinero:.2f}")

        # Mostrar el detalle de redenciones
        print("\nDetalle de Redenciones:")
        with shelve.open(self.redenciones_db_name) as db_redenciones:
            redenciones_encontradas = False
            for id_factura, redencion in db_redenciones.items():
                if redencion["usuario"] == usuario:
                    redenciones_encontradas = True
                    fecha = redencion["fecha"].strftime('%Y-%m-%d %H:%M:%S')
                    puntos_redimidos = redencion["puntos_redimidos"]
                    print(f"- Fecha: {fecha}, ID Factura: {id_factura}, Puntos Redimidos: {puntos_redimidos}")
            
            if not redenciones_encontradas:
                print("No se encontraron redenciones para este usuario.")

    def menu_consulta_historial(self):
        while True:
            print("\n--- Menú de Consulta de Historial de Puntos ---")
            print("1. Consultar historial de puntos de un usuario")
            print("2. Volver al Menu General")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.consultar_historial_puntos()
            elif opcion == "2":
                print("Volviendo al Menu General...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

# Ejemplo de uso del menú
if __name__ == "__main__":
    consulta_historial = ConsultaHistoricoPts()
    consulta_historial.menu_consulta_historial()