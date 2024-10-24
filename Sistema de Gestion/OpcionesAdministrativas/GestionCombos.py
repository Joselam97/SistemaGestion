import shelve
#importo de GestionAlimento para incluirlos a los combos
from GestionAlimento import GestionAlimento
class GestionCombo:
    #db_name es la variable que alamacena el nombre del archivo en la base de datos
    def __init__(self, db_name='combos.db', gestion_alimento=None):
        self.db_name = db_name
        self.gestion_alimento = gestion_alimento  


#funcion para incluir combo, solicitando nombre,costo,margen_ganancia y alimentos
    def incluir_combo(self, nombre, costo, margen_ganancia, alimentos):
        #guarda cada combo en la base de datos 'db_name' con en una variable llamada 'db_combos'
        with shelve.open(self.db_name) as db_combos:
            
            #en caso de existir un combo con ese nombre, da error
            if nombre in db_combos:
                print(f"Error: Ya existe un combo con el nombre '{nombre}'.")
                return
            
            #en caso de ingresar un dato de margen_ganancia fuera del rango da error
            if margen_ganancia < 0 or margen_ganancia > 100:
                print("Error: El margen de ganancia debe estar entre 0 y 100.")
                return
            
            #en caso de cumplir con los requisitos, solicita la info para agregar al combo
            precio_venta = costo * (1 + margen_ganancia / 100)
            #diccionario de la informacion del alimento para guardar en 'db_combos'
            db_combos[nombre] = {
                'costo': costo,
                'margen_ganancia': margen_ganancia,
                'precio_venta': precio_venta,
                'alimentos': alimentos 
            }
            print(f"Combo '{nombre}' agregado con éxito.")



    def existe_combo(self, nombre):
        with shelve.open(self.db_name) as db_combos:
            return nombre in db_combos  
        

#funcion para eliminar combos en funcion de su nombre
    def eliminar_combo(self, nombre):
        with shelve.open(self.db_name) as db_combos:
            
            #en caso de no existir el nombre del combo, da error
            if nombre not in db_combos:
                print(f"Error: El combo '{nombre}' no existe.")
                return
            
            if self.combo_asociado(nombre):
                print(f"Error: No se puede eliminar el combo '{nombre}' porque está asociado a una orden o factura.")
                return
            
            #si el combo existe y no esta asociado, lo elimina
            del db_combos[nombre]
            print(f"Combo '{nombre}' eliminado con éxito.")


#funcion para modificar combo, en caso de existir el nombre, nuevos costos, margen_ganancia y alimentos no sean null
    def modificar_combo(self, nombre, nuevo_costo=None, nuevo_margen_ganancia=None, nuevos_alimentos=None):
        with shelve.open(self.db_name) as db_combos:
            if nombre not in db_combos:
                print(f"Error: El combo '{nombre}' no existe.")
                return
        
            combo = db_combos[nombre]

            # Modificación del costo
            if nuevo_costo is not None:
                try:
                    nuevo_costo = float(nuevo_costo) if nuevo_costo is not None else combo['costo']
                    combo['costo'] = nuevo_costo
                except ValueError:
                    print("Error: El costo debe ser un número.")
                    return

            # Modificación del margen de ganancia
            if nuevo_margen_ganancia is not None:
                try:
                    nuevo_margen_ganancia = float(nuevo_margen_ganancia)
                    if nuevo_margen_ganancia < 0 or nuevo_margen_ganancia > 100:
                        print("Error: El margen de ganancia debe estar entre 0 y 100.")
                        return
                    combo['margen_ganancia'] = nuevo_margen_ganancia
                except ValueError:
                    print("Error: El margen de ganancia debe ser un número.")
                    return

            # Modificación de alimentos utilizando el diccionario nuevos_alimentos pasado como parámetro
            if nuevos_alimentos:
                for alimento, cantidad in nuevos_alimentos.items():
                    if cantidad < 0:
                        print(f"Error: La cantidad para el alimento '{alimento}' debe ser un número positivo.")
                        return
                    if alimento in combo['alimentos']:
                        combo['alimentos'][alimento] = cantidad
                    else:
                        print(f"Error: El alimento '{alimento}' no está en el combo.")
                        return

            # Actualizar el precio de venta si el costo y margen existen
            if 'costo' in combo and 'margen_ganancia' in combo:
                combo['precio_venta'] = combo['costo'] * (1 + combo['margen_ganancia'] / 100)

            # Almacenar el combo modificado en la base de datos
            db_combos[nombre] = combo
            print(f"Combo '{nombre}' modificado con éxito.")

#funcion para mostrar combos guardados
    def mostrar_combos(self):
        #imprime la informacion guardada en 'db_combos'
        with shelve.open(self.db_name) as db_combos:
            
            #en caso de no haber nada registrado
            if not db_combos:
                print("No hay combos registrados.")
            #en caso contrario    
            else:
                print("\nCombos registrados:")
                #itera por cada uno de los datos anteriormente solicitados para guardar cada combo en 'db_combos'
                for nombre, datos in db_combos.items():
                    print(f"- {nombre}: Costo: {datos['costo']} colones, "
                          f"Margen de ganancia: {datos['margen_ganancia']}%, Precio de venta: {datos['precio_venta']} colones")
                    print("  Alimentos incluidos:")
                    #itera por cada alimento que se incluyo en el combo
                    for alimento, cantidad in datos['alimentos'].items():
                        print(f"    - {alimento}: {cantidad}")

    #verifica si el combo esta asociado a alguna orden o factura en funcion de su nombre para no poder hacer cambios 
    def combo_asociado(self, nombre):
        return False  

#funcion para mostrar el menu
def menu_combo(gestion_alimento):
    gestion_combo = GestionCombo(gestion_alimento=gestion_alimento)

    while True:
        print("\n--- Menú de Gestión de Combos ---")
        print("1. Incluir Combo")
        print("2. Eliminar Combo")
        print("3. Modificar Combo")
        print("4. Mostrar Combos")
        print("5. Volver al Menu Administrativo")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del combo: ").strip()
    
    # Validación del costo
            while True:
                costo_input = input("Ingrese el costo del combo: ").strip()
                try:
                    costo = float(costo_input)
                    if costo < 0:
                        print("Error: El costo no puede ser negativo. Inténtelo nuevamente.")
                        continue
                    break  # Salir del bucle si la entrada es válida
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido para el costo.")
    
    # Validación del margen de ganancia
            while True:
                margen_input = input("Ingrese el margen de ganancia (en %): ").strip()
                try:
                    margen_ganancia = float(margen_input)
                    if margen_ganancia < 0 or margen_ganancia > 100:
                        print("Error: El margen de ganancia debe estar entre 0 y 100. Inténtelo nuevamente.")
                        continue
                    break  # Salir del bucle si la entrada es válida
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido para el margen de ganancia.")

    # Mostrar alimentos disponibles
            gestion_alimento.mostrar_alimentos()
    
            alimentos = {}
            while True:
                nombre_alimento = input("Ingrese el nombre del alimento a incluir en el combo (o 'terminar'): ").strip()
                if nombre_alimento.lower() == 'terminar':
                    break
        # Validación de la cantidad de alimentos
                while True:
                    cantidad_input = input(f"Ingrese la cantidad de '{nombre_alimento}' a incluir: ").strip()
                    try:
                        cantidad = int(cantidad_input)
                        if cantidad < 0:
                            print("Error: La cantidad no puede ser negativa. Inténtelo nuevamente.")
                            continue
                        break  # Salir del bucle si la entrada es válida
                    except ValueError:
                        print("Error: Por favor, ingrese un valor numérico válido para la cantidad.")

                alimentos[nombre_alimento] = cantidad
    
    # Llamada a la función para incluir el combo
            gestion_combo.incluir_combo(nombre, costo, margen_ganancia, alimentos)
            

        elif opcion == "2":
            nombre = input("Ingrese el nombre del combo a eliminar: ")
            gestion_combo.eliminar_combo(nombre)

        elif opcion == "3":
            gestion_combo.mostrar_combos()
            print("\n --- Combos registrados --- \n")
            nombre = input("Ingrese el nombre del combo a modificar: ")
            if not gestion_combo.existe_combo(nombre):
                print("Error: El combo no está registrado. Por favor, inténtelo nuevamente.")
                continue
            
            nuevo_costo = None
            while nuevo_costo is None:
                nuevo_costo_input = input("Ingrese el nuevo costo (escriba 'no' si desea dejarlo igual): ")
                if nuevo_costo_input.strip().lower() == "no":
                    nuevo_costo = None
                    break
                else:
                    try:
                        nuevo_costo = float(nuevo_costo_input)
                    except ValueError:
                        print("Error: Por favor, ingrese un valor numérico válido para el costo.")

            nuevo_margen_ganancia = None
            while nuevo_margen_ganancia is None:
                nuevo_margen_ganancia_input = input("Ingrese el nuevo margen de ganancia en % (escriba 'no' si desea dejarlo igual): ")
                if nuevo_margen_ganancia_input.strip().lower() == "no":
                    nuevo_margen_ganancia = None
                    break
                else:
                    try:
                        nuevo_margen_ganancia = float(nuevo_margen_ganancia_input)
                        if nuevo_margen_ganancia < 0 or nuevo_margen_ganancia > 100:
                            print("Error: El margen de ganancia debe estar entre 0 y 100.")
                            nuevo_margen_ganancia = None
                    except ValueError:
                        print("Error: Por favor, ingrese un valor numérico válido para el margen de ganancia.")

            nuevos_alimentos = {}
            
            while True:
                nombre_alimento = input("Ingrese el nombre del alimento a modificar en el combo (o 'terminar'): ")
                if nombre_alimento.lower() == 'terminar':
                    break
                if not nombre_alimento.isalnum() or not nombre_alimento.strip():
                    print("Error: El nombre del alimento debe ser alfanumérico y no debe estar vacío.")
                    continue
                
                try:
                    cantidad = int(input(f"Ingrese la nueva cantidad de '{nombre_alimento}': "))
                    if cantidad < 0:
                        print("Error: La cantidad debe ser un número entero positivo.")
                        continue
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido para la cantidad.")
                    continue

                nuevos_alimentos[nombre_alimento] = cantidad
            
            gestion_combo.modificar_combo(nombre, nuevo_costo, nuevo_margen_ganancia, nuevos_alimentos)

        elif opcion == "4":
            #muestra los combos guardados
            gestion_combo.mostrar_combos()

        elif opcion == "5":
            print("Volviendo al Menú Administrativo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Iniciar el menú
if __name__ == "__main__":
      # Asegúrate de tener importada la clase correspondiente

#gestion_alimento es la variable que almacena la clase 'GestionAlimento' para usarla e importar datos
    gestion_alimento = GestionAlimento()
    menu_combo(gestion_alimento)
