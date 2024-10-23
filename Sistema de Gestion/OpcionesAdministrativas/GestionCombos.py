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
            
            #en caso de no existir el nombre del combo, da error
            if nombre not in db_combos:
                print(f"Error: El combo '{nombre}' no existe.")
                #regresa debido al error
                return
            
            #'combo' lo asocia a algun nombre de combo en 'db_combos'
            combo = db_combos[nombre]

            #si se ingresa un nuevo costo, lo modifica
            if nuevo_costo is not None:
                combo['costo'] = nuevo_costo

            #si se ingresa un nuevo margen_ganancia, lo modifica
            if nuevo_margen_ganancia is not None:
                #solicita que el margen este entre el rango para que no de error
                if nuevo_margen_ganancia < 0 or nuevo_margen_ganancia > 100:
                    print("Error: El margen de ganancia debe estar entre 0 y 100.")
                    #regresa debido al error
                    return
                
                #modifica el margen de ganancia
                combo['margen_ganancia'] = nuevo_margen_ganancia
                
            #si se ingresa un alimento lo agrega    
            if nuevos_alimentos is not None:
                combo['alimentos'] = nuevos_alimentos

            #Actualiza el combo con la nueva informacion brindada
            combo['precio_venta'] = combo['costo'] * (1 + combo['margen_ganancia'] / 100)
            #agrega informacion actualizada a 'db_combos' donde el nombre del combo coincide con el que se ingreso
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
        print("5. Volver al Menú Administrativo")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del combo: ")
            costo = float(input("Ingrese el costo del combo: "))
            margen_ganancia = float(input("Ingrese el margen de ganancia (en %): "))
            
            #importa funcion 'mostrar_alimentos' de GestionAlimento para mostrar alimentos disponibles anteriormente guardados
            gestion_alimento.mostrar_alimentos()
            alimentos = {} #diccionario para guardar alimentos
            while True:
                #itera cada vez para ingresar un alimento guardado hasta que se escriba 'terminar'
                nombre_alimento = input("Ingrese el nombre del alimento a incluir en el combo (o 'terminar'): ")
                #permite escribir 'terminar' sin importar el tipo de case
                if nombre_alimento.lower() == 'terminar':
                    #sale del loop
                    break
                cantidad = int(input(f"Ingrese la cantidad de '{nombre_alimento}' a incluir: "))
                alimentos[nombre_alimento] = cantidad
            
            #incluye a la variable 'gestion_combo' asociada a la clase 'GestionCombo' el combo con los datos brindados por medio de la funcion 'incluir_combo' 
            gestion_combo.incluir_combo(nombre, costo, margen_ganancia, alimentos)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del combo a eliminar: ")
            gestion_combo.eliminar_combo(nombre)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del combo a modificar: ")
            nuevo_costo = input("Ingrese el nuevo costo (deje en blanco si no desea cambiar): ")
            #convierte el nuevo costo a float en caso de modificarlo sino, no lo modifica
            nuevo_costo = float(nuevo_costo) if nuevo_costo else None
            
            nuevo_margen_ganancia = input("Ingrese el nuevo margen de ganancia (en %, deje en blanco si no desea cambiar): ")
            nuevo_margen_ganancia = float(nuevo_margen_ganancia) if nuevo_margen_ganancia else None
            
            nuevos_alimentos = {} #diccionario para guardar alimentos nuevos
            gestion_combo.mostrar_combos()  #muestra los combos actuales para referencia
            while True:
                nombre_alimento = input("Ingrese el nombre del alimento a modificar en el combo (o 'terminar'): ")
                if nombre_alimento.lower() == 'terminar':
                    break
                cantidad = int(input(f"Ingrese la nueva cantidad de '{nombre_alimento}': "))
                nuevos_alimentos[nombre_alimento] = cantidad
            
            #modifica el combo con la info brindada usando la variable y llamando a la funcion
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
