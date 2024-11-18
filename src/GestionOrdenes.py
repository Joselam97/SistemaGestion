import shelve
from datetime import datetime
from CrearUsuario import CrearUsuario  # Se asume que tienes una clase CrearUsuario implementada
from GestionAlimento import GestionAlimento
from GestionCombos import GestionCombo

class GestionOrdenes(CrearUsuario, GestionAlimento, GestionCombo):
    #inicializa la clase y define la base de datos de ordenes
    def __init__(self):
        super().__init__()
        #el argumento self crea la base de datos con el valor 'ordenes_db'
        self.ordenes_db_name = 'ordenes.db'
    
    #funcion para solicitar el nombre de usuario
    def solicitar_usuario(self):
        while True:
            usuario = input("Ingrese su nombre de usuario (o escriba 'volver' para regresar al menu): ")
            if usuario.lower() == "volver":
                #regresa si el usuario decide volver
                return None 
            #verifica si el usuario existe en la base de datos
            if self.verificar_usuario(usuario):
                print(f"Usuario '{usuario}' verificado exitosamente.")
                return usuario
            else:
                print("El usuario ingresado no existe. Por favor, intente de nuevo.")
    
    #genera un identificador unico para cada orden, basado en la fecha
    def generar_identificador_orden(self,usuario):
        #obtiene la fecha actual
        fecha_hoy = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        
        #retorna un identificador unico usando la fecha en formato yyyy-mm-dd y hhmmss
        return f"ORD-{fecha_hoy}"
    
    #crea una nueva orden y la guarda en la base de datos
    def crear_orden(self):
        #solicita el usuario
        usuario = self.solicitar_usuario()
        if usuario is None:
            return
        print(f"Usuario en crear_orden: '{usuario}'")

        #genera un identificador unico para la orden
        id_orden = self.generar_identificador_orden(usuario)
        #obtiene la fecha y hora actual
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        #estructura de la nueva orden con todos los detalles necesarios
        nueva_orden = {
            "usuario": usuario,
            "fecha_hora": fecha_hora,
            "combos": {},
            "alimentos": {},
            "facturada": False
        }
        print(f"Creando nueva orden con usuario: '{nueva_orden['usuario']}'")

        #guarda la nueva orden en la base de datos
        with shelve.open(self.ordenes_db_name, writeback=True) as db_ordenes:
            if usuario not in db_ordenes:
                #crea un diccionario vacío para el usuario si no existe
                db_ordenes[usuario] = {}  
                #guarda la orden bajo la clave del usuario
            db_ordenes[usuario][id_orden] = nueva_orden  
            print(f"Orden creada con ID: {id_orden} para el usuario {usuario}.")
    
        self.editar_orden(usuario,id_orden)
    
    #muestra las ordenes de un usuario, filtrando por si estan facturadas o no    
    def mostrar_ordenes_usuario(self, usuario, facturadas=False):
        ordenes_ids = []
        with shelve.open(self.ordenes_db_name) as db_ordenes:
            if usuario in db_ordenes:
                for id_orden, datos in db_ordenes[usuario].items():
                    if datos["facturada"] == facturadas:
                        print(f"ID Orden: {id_orden}, Fecha y Hora: {datos['fecha_hora']}")
                        ordenes_ids.append(id_orden)

                #si no se encontraron ordenes, muestra un mensaje indicando el resultado
            if not ordenes_ids:
                if facturadas:
                    print("No se encontraron ordenes facturadas.")

        #retorna la lista de identificadores de ordenes
        return ordenes_ids
    
    #funcion para editar una orden especifica
    def editar_orden(self, usuario, id_orden):
        #abre la base de datos de ordenes
        with shelve.open(self.ordenes_db_name, writeback=True) as db_ordenes:
            #verifica si el identificador de la orden existe
            if usuario not in db_ordenes or id_orden not in db_ordenes[usuario]:
                print("El ID de la orden no existe.")
                return
 
            #obtiene la orden a editar
            orden = db_ordenes[usuario][id_orden]
            #verifica si la orden ya fue facturada
            if orden["facturada"]:
                print("La orden ya ha sido facturada y no se puede editar.")
                return

            #menu de edicion de la orden
            while True:
                print("\n--- Edicion de Orden ---")
                print("1. Incluir combo")
                print("2. Disminuir combo")
                print("3. Incluir alimento")
                print("4. Disminuir alimento")
                print("5. Volver al menu principal")

                opcion = input("Seleccione una opcion: ")
                #llama a la funcion correspondiente segun la opcion
                if opcion == "1":
                    self.incluir_combo(usuario, id_orden, db_ordenes)
                elif opcion == "2":
                    self.disminuir_combo(usuario, id_orden, db_ordenes)
                elif opcion == "3":
                    self.incluir_alimento(usuario, id_orden, db_ordenes)
                elif opcion == "4":
                    self.disminuir_alimento(usuario, id_orden, db_ordenes)
                elif opcion == "5":
                    print("Regresando al menu principal.")
                    break
                else:
                    print("Opcion no valida. Intente de nuevo.")

    #funcion para incluir un como en una orden
    def incluir_combo(self, usuario, id_orden, db_ordenes):
        #abre la base de datos de combos
        with shelve.open('combos.db') as db_combos:
            #obtiene la orden a modificar
            orden = db_ordenes[usuario][id_orden]

            #muestra todos los combos disponibles, por medio de sus claves que estan guardadas en un diccionario
            print("\n--- Combos Disponibles ---")
            for combo in db_combos.keys():
                print(f"- {combo}")

            #solicita el nombre del combo a incluir
            combo_seleccionado = input("Ingrese el nombre del combo a incluir (o 'volver' para regresar): ")
            if combo_seleccionado.lower() == "volver":
                return

            #verifica si el combo existe en la base de datos
            if combo_seleccionado in db_combos:
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad de este combo: "))
                        if cantidad <= 0:
                            print("Error: Debe ingresar solo cantidades positivas.")
                            continue #vuelve a solicitar la cantidad
                        break  #sale del bucle si la entrada es valida
                    except ValueError:
                        print("Error: Debe ingresar un numero entero para la cantidad.")

                #si el combo ya está en la orden, aumenta la cantidad
                if combo_seleccionado in orden["combos"]:
                    orden["combos"][combo_seleccionado] += cantidad
                else:
                    orden["combos"][combo_seleccionado] = cantidad
            
            #actualiza la orden en la base de datos
                db_ordenes[usuario][id_orden] = orden
                print(f"Combo '{combo_seleccionado}' incluido con exito en la orden.")
            else:
                print("El combo ingresado no existe. Intente de nuevo.")
            
            
    #funcion para disminuir la cantidad de un combo en una orden
    def disminuir_combo(self, usuario, id_orden, db_ordenes):
        #obtiene la orden a modificar
        orden = db_ordenes[usuario][id_orden]
        print("\n--- Combos en la Orden ---")
        #muestra los combos actuales en la orden, iterando por cada uno
        for combo, cantidad in orden["combos"].items():
            print(f"- {combo}: {cantidad}")

        #solicita el nombre del combo a disminuir
        combo_seleccionado = input("Ingrese el nombre del combo a disminuir (o 'volver' para regresar): ")
        if combo_seleccionado.lower() == "volver":
            return

        #verifica si el combo esta en la orden
        if combo_seleccionado in orden["combos"]:
            while True:
                try:
                    #solicita la cantidad que desea disminuir y asegura que sea un entero
                    cantidad = int(input("Ingrese la cantidad a disminuir: "))
                    if cantidad < 0:
                        print("Error: Debe ingresar solo cantidades positivas.")
                        continue
                    break  #sale del bucle si la entrada es valida
                except ValueError:
                    print("Error: Debe ingresar un numero entero para la cantidad a disminuir.")

                #si la cantidad a disminuir es igual o mayor a la cantidad actual, elimina el combo
            if cantidad >= orden["combos"][combo_seleccionado]:
                del orden["combos"][combo_seleccionado]
                print(f"Combo '{combo_seleccionado}' eliminado de la orden.")
            else:
            #si la cantidad a disminuir es menor, simplemente resta la cantidad
                orden["combos"][combo_seleccionado] -= cantidad
                print(f"Combo '{combo_seleccionado}' disminuido en la orden.")

        #actualiza la orden en la base de datos
            db_ordenes[usuario][id_orden] = orden
        else:
            print("El combo ingresado no esta en la orden.")

    #funcion para incluir un alimento en una orden
    def incluir_alimento(self, usuario, id_orden, db_ordenes):
        #abre la base de datos de alimentos
        with shelve.open('alimentos.db') as db_alimentos:
            #obtiene la orden a modificar
            orden = db_ordenes[usuario][id_orden]

            #muestra todos los alimentos disponibles
            print("\n--- Alimentos Disponibles ---")
            for alimento in db_alimentos.keys():
                print(f"- {alimento}")

            #solicita el nombre del alimento a incluir
            alimento_seleccionado = input("Ingrese el nombre del alimento a incluir (o 'volver' para regresar): ")
            if alimento_seleccionado.lower() == "volver":
                return
           
            #verifica si el alimento existe en la base de datos
            if alimento_seleccionado in db_alimentos:
                while True:
                    try:
                    #solicita la cantidad y asegura que sea un entero
                        cantidad = int(input("Ingrese la cantidad de este alimento: "))
                        if cantidad <= 0:
                            print("Error: Debe ingresar solo cantidades positivas.")
                            continue #vuelve a solicitar la cantidad
                        break  #rompe el bucle si la entrada es valida
                    except ValueError:
                        print("Error: Debe ingresar un numero entero para la cantidad.")

                #si el alimento ya está en la orden, aumenta la cantidad
                if alimento_seleccionado in orden["alimentos"]:
                    orden["alimentos"][alimento_seleccionado] += cantidad
                else:
                    orden["alimentos"][alimento_seleccionado] = cantidad

                #actualiza la orden en la base de datos
                db_ordenes[usuario][id_orden] = orden
                print(f"Alimento '{alimento_seleccionado}' incluido con exito en la orden.")
            else:
                print("El alimento ingresado no existe. Intente de nuevo.")

    #funcion para disminuir la cantidad de un alimento en una orden
    def disminuir_alimento(self,usuario, id_orden, db_ordenes):
        #obtiene la orden que se va a modificar
        orden = db_ordenes[usuario][id_orden]
        print("\n--- Alimentos en la Orden ---")
        #muestra todos los alimentos que ya estan en la orden
        for alimento, cantidad in orden["alimentos"].items():
            print(f"- {alimento}: {cantidad}")
 
 #solicita al usuario el alimento que desea disminuir
        alimento_seleccionado = input("Ingrese el nombre del alimento a disminuir (o 'volver' para regresar): ")
        if alimento_seleccionado.lower() == "volver":
            return

#comprueba si el alimento ingresado esta en la orden
        if alimento_seleccionado in orden["alimentos"]:
            while True:
                try:
                    #solicita la cantidad que desea disminuir y asegura que sea un entero
                    cantidad = int(input("Ingrese la cantidad a disminuir: "))
                    if cantidad < 0:
                        print("Error: Debe ingresar solo cantidades positivas.")
                        continue
                    break  #sale del bucle si la entrada es valida
                except ValueError:
                    print("Error: Debe ingresar un numero entero para la cantidad a disminuir.")

                #si la cantidad a disminuir es igual o mayor a la cantidad actual, elimina el alimento
            if cantidad >= orden["alimentos"][alimento_seleccionado]:
                del orden["alimentos"][alimento_seleccionado]
                print(f"Alimento '{alimento_seleccionado}' eliminado de la orden.")
            else:
                #si la cantidad a disminuir es menor, simplemente resta la cantidad
                orden["alimentos"][alimento_seleccionado] -= cantidad
                print(f"Alimento '{alimento_seleccionado}' disminuido en la orden.")
        
            #actualiza la orden con la nueva cantidad de alimentos
            db_ordenes[usuario][id_orden] = orden
        else:
            print("El alimento ingresado no esta en la orden.")

    #funcion para consultar las ordenes de un usuario
    def consultar_ordenes(self):
        #solicita el usuario
        usuario = self.solicitar_usuario()
        if usuario is None:
            return
        print(f"Usuario en consultar_ordenes: '{usuario}'")

        #abre la base de datos de ordenes para mostrar todas las ordenes del usuario 'x'
        with shelve.open(self.ordenes_db_name) as db_ordenes:
            print(f"\n--- Ordenes del usuario '{usuario}' ---")
            if usuario in db_ordenes:
                for id_orden, datos in db_ordenes[usuario].items():
                    print(f"\nID Orden: {id_orden}")
                    print(f"Fecha y Hora: {datos['fecha_hora']}")
                    print("Combos:")
                    for combo, cantidad in datos["combos"].items():
                        print(f" - {combo}: {cantidad}")
                    print("Alimentos:")
                    for alimento, cantidad in datos["alimentos"].items():
                        print(f" - {alimento}: {cantidad}")
                    print(f"Facturada: {'Si' if datos['facturada'] else 'No'}")
            else:
                print("No se encontraron ordenes para este usuario.")
            print("\nConsulta completada.")

#funcion para facturar una orden
    def facturar_orden(self,usuario, id_orden):
        #abre la base de datos de ordenes y permite hacer modificacions
        with shelve.open(self.ordenes_db_name, writeback=True) as db_ordenes:
            #comprueba si el usuario de la orden existe
            if usuario not in db_ordenes or id_orden not in db_ordenes[usuario]:
                print("El usuario de la orden no existe")
                return

#verifica si el ID de la orden existe para ese usuario
            if id_orden not in db_ordenes[usuario]:
                print("El ID de la orden no existe para el usuario")
                return

#marca la orden como facturada
            if db_ordenes[usuario][id_orden]["facturada"]:
                print("La orden ya ha sido facturada")
                return
            
            #marca la orden como facturada
            db_ordenes[usuario][id_orden]["facturada"] = True
            print(f"La orden con el ID {id_orden} ha sido facturada exitosamente. ")
                

#funcion para eliminar la orden
    def eliminar_orden(self, usuario, id_orden):
        #abre la base de datos de ordenes y permite hacer modificaciones
        with shelve.open(self.ordenes_db_name, writeback=True) as db_ordenes:
            #comprueba si el user esta en ordenes
            if usuario not in db_ordenes:
                print("El Usuario no existe")
                return

            # verifica si el ID de la orden existe para ese usuario
            if id_orden not in db_ordenes[usuario]:
                print("El ID de la orden no existe para el usuario.")
                return

            if not db_ordenes[usuario][id_orden]["combos"] and not db_ordenes[usuario][id_orden]["alimentos"]:
                del db_ordenes[usuario][id_orden]
                print(f"La orden con ID {id_orden} ha sido eliminada exitosamente.")
            else:
                print("No se puede eliminar una orden que contiene alimentos o combos.")
                
                
#menu principal para gestionar las ordenes
    def menu_ordenes(self):
        while True:
            print("\n--- Menu de Gestion de Ordenes ---")
            print("1. Crear Orden")
            print("2. Editar Orden")
            print("3. Consultar Ordenes")
            print("4. Facturar Orden")
            print("5. Eliminar Orden")
            print("6. Volver al Menu Administrativo")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.crear_orden()
                
                
            elif opcion == "2":
                usuario = self.solicitar_usuario()
                if usuario:
                    ordenes = self.mostrar_ordenes_usuario(usuario, facturadas=False)
                    if ordenes:
                        id_orden = input("Ingrese el identificador de la orden a editar: ")
                        if id_orden in ordenes:
                            self.editar_orden(usuario,id_orden)
                        else:
                            print("Orden no valida seleccionada.")
                            
                            
            elif opcion == "3":
                self.consultar_ordenes()
                
                
            elif opcion == "4":
                usuario = self.solicitar_usuario()
                if usuario:
                    ordenes = self.mostrar_ordenes_usuario(usuario, facturadas=False)
                    if ordenes:
                        id_orden = input("Ingrese el identificador de la orden a facturar: ")
                        if id_orden in ordenes:
                            self.facturar_orden(usuario,id_orden)
                        else:
                            print("Orden no valida seleccionada.")
                            
                            
            elif opcion == "5":
                usuario = self.solicitar_usuario()
                if usuario:
                    ordenes = self.mostrar_ordenes_usuario(usuario, facturadas=False)
                    if ordenes:
                        id_orden = input("Ingrese el identificador de la orden a eliminar: ")
                        if id_orden in ordenes:
                            self.eliminar_orden(usuario,id_orden)
                        else:
                            print("Orden no valida seleccionada.")
                            
                            
            elif opcion == "6":
                print("\n Volviendo al Menu Administrativo...")
                break
            else:
                print("\n Opcion no valida. Intente de nuevo.")