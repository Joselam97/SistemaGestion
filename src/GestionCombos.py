import shelve
#importo de GestionAlimento para incluirlos a los combos
from GestionAlimento import GestionAlimento
class GestionCombo:
    #db_name es la variable que alamacena el nombre del archivo en la base de datos
    def __init__(self, db_name='combos.db', gestion_alimento=None):
        self.db_name = db_name
        self.gestion_alimento = gestion_alimento  
        
    
    def obtener_info_combo(self, nombre):
        #Devuelve el precio de venta y detalles del combo
        with shelve.open(self.db_name) as db_combos:
            return db_combos.get(nombre, None)


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
            
            if not alimentos:
               print(f"Error: No se puede crear el combo '{nombre}' sin alimentos incluidos.")
               return
           
           
            with shelve.open(self.gestion_alimento.db_name) as db_alimentos:
                for alimento in alimentos:
                    if alimento not in db_alimentos:
                        print(f"Error: El alimento '{alimento}' no existe en la lista de alimentos. No se puede crear el combo.")
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

            #agrega nuevo margen de ganancia despues de la modificaion
            if nuevo_margen_ganancia is not None:
                try:
                    nuevo_margen_ganancia = float(nuevo_margen_ganancia)
                    if nuevo_margen_ganancia < 0 or nuevo_margen_ganancia > 100:
                        print("Error: El margen de ganancia debe estar entre 0 y 100.")
                        return
                    combo['margen_ganancia'] = nuevo_margen_ganancia
                #maneja el error de tipo de dato, solo permite integers
                except ValueError:
                    print("Error: El margen de ganancia debe ser un numero.")
                    return

            #modifica la cantidad de alimento escogido
            if nuevos_alimentos:
                for alimento, cantidad in nuevos_alimentos.items():
                    #pide que sea un numero mayor a 0
                    if cantidad < 0:
                        print(f"Error: La cantidad para el alimento '{alimento}' debe ser un número positivo.")
                        return
                    #si el alimento se encuentra en el combo lo agrega
                    if alimento in combo['alimentos']:
                        combo['alimentos'][alimento] = cantidad
                    else:
                        print(f"Error: El alimento '{alimento}' no está en el combo.")
                        return

            #modifica el precio de venta si el costo y margen existen
            if 'costo' in combo and 'margen_ganancia' in combo:
                combo['precio_venta'] = combo['costo'] * (1 + combo['margen_ganancia'] / 100)

            #guarda el combo modificado en la base de datos
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

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            while True:
                nombre = input("\nIngrese el nombre del combo (o 'volver' para cancelar): ").strip()
                if nombre.lower() == 'volver':
                    print("Operacion cancelada. Volviendo al menu de opciones administrativas.")
                    return
                
                #verifica si el nombre del combo ya existe
                if gestion_combo.existe_combo(nombre):
                    print(f"Error: Ya existe un combo con el nombre '{nombre}'. Por favor, elija otro nombre.")
                else:
                    #si el nombre es válido, salir del bucle
                    break
            
    
            while True:
                #Solicita el costo del combo y elimina espacios en blanco al inicio y al final
                costo_input = input("\nIngrese el costo del combo: ").strip()
                try:
                    #convierte la entrada a float
                    costo = float(costo_input)
                    #verifica que el costo no sea negativo
                    if costo < 0:
                        print("Error: El costo no puede ser negativo. Intentelo nuevamente.")
                        #pide el costo nuevamente
                        continue
                    #sale del bucle si el costo es valido
                    break  
                #maneja errores si la entrada no es un numero valido
                except ValueError:
                    print("Error: Por favor, ingrese un valor numerico valido para el costo.")
           
    
    #bucle para solicitar el margen de ganancia
            while True:
                #solicita el margen de ganancia y elimina espacios en blanco al incio y final
                margen_input = input("\nIngrese el margen de ganancia (en %): ").strip()
                try:
                    #convierte la entrada a float
                    margen_ganancia = float(margen_input)
                    #verifica que el margen este en el rango de 0 a 100
                    if margen_ganancia < 0 or margen_ganancia > 100:
                        print("Error: El margen de ganancia debe estar entre 0 y 100. Intentelo nuevamente.")
                        #pide el margen nuevamente si no esta en el rango
                        continue
                    #sale del bucle si el margen es valido
                    break  
                #maneja errores si la entrada no es un numero valido
                except ValueError:
                    print("Error: Por favor, ingrese un valor numerico valido para el margen de ganancia.")
            
    #muestra los alimentos disponibles en la gestion
            gestion_alimento.mostrar_alimentos()
    
    #inicializa un diccionario para almacenar los alimentos incluidos en el combo
            alimentos = {}
            while True:
                #solicita el nombre de alimento a incluir en el combo
                nombre_alimento = input("\nIngrese el nombre del alimento a incluir en el combo (o 'terminar'): ").strip()
                if nombre_alimento.lower() == 'terminar':
                    #sale del bucle si se ingresa 'terminar'
                    break
                
                #verifica si el alimento existe en la base de datos de alimentos
                if not gestion_alimento.obtener_info_alimento(nombre_alimento):
                    #print(f"Error: El alimento '{nombre_alimento}' no existe en la lista de alimentos. Inténtelo nuevamente.")
                    continue
        
                while True:
                    #solicita la cantidad de unidades del alimento a incluir en el combo
                    cantidad_input = input(f"\nIngrese la cantidad de '{nombre_alimento}' a incluir: ").strip()
                    try:
                        #convierte la entrada a entero
                        cantidad = int(cantidad_input)
                        #verifica que la cantidad no sea negativa
                        if cantidad < 0:
                            print("Error: La cantidad no puede ser negativa. Intentelo nuevamente.")
                            #pide la cantidad nuevamente si es negativa
                            continue
                        #sale del bucle si la cantidad no es valida
                        break  
                    except ValueError:
                        #maneja errores si la entrada no es un numero valido
                        print("Error: Por favor, ingrese un valor numerico valido para la cantidad.")
        

#agrega el alimento y la cantidad al diccionario de alimentos
                alimentos[nombre_alimento] = cantidad
    
    #incluye el combo en la gestion con los alimentos ingresados
            gestion_combo.incluir_combo(nombre, costo, margen_ganancia, alimentos)
            
#eliminacion de un combo
        elif opcion == "2":
            nombre = input("\nIngrese el nombre del combo a eliminar: ")
            gestion_combo.eliminar_combo(nombre)

#modifica combos existenes
        elif opcion == "3":
            gestion_combo.mostrar_combos()
            print("\n --- Combos registrados --- \n")
            nombre = input("Ingrese el nombre del combo a modificar: ")
            #verifica si el combo existe
            if not gestion_combo.existe_combo(nombre):
                print("Error: El combo no esta registrado. Por favor, intentelo nuevamente.")
                continue
            
            #solicita el nuevo costo del combo, en caso de querer cambiar
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
                        print("Error: Por favor, ingrese un valor numerico valido para el costo.")

#solicita el nuevo margen de ganancia 
            nuevo_margen_ganancia = None
            while nuevo_margen_ganancia is None:
                nuevo_margen_ganancia_input = input("Ingrese el nuevo margen de ganancia en % (escriba 'no' si desea dejarlo igual): ")
                if nuevo_margen_ganancia_input.strip().lower() == "no":
                    #sigue sin haber valor en 'nuevo_margen_ganacia' debido a no modificarlo
                    nuevo_margen_ganancia = None
                    #sale del bucle 
                    break
                else:
                    try:
                        nuevo_margen_ganancia = float(nuevo_margen_ganancia_input)
                        if nuevo_margen_ganancia < 0 or nuevo_margen_ganancia > 100:
                            print("Error: El margen de ganancia debe estar entre 0 y 100.")
                            nuevo_margen_ganancia = None
                            #maneja el error en caso de ingresar un margen fuera del rango
                    except ValueError:
                        print("Error: Por favor, ingrese un valor numerico válido para el margen de ganancia.")

#solicita nuevos alimentos al combo y los guarda en un diccionario
            nuevos_alimentos = {}
            
            while True:
                nombre_alimento = input("Ingrese el nombre del alimento a modificar en el combo (o 'terminar'): ")
                if nombre_alimento.lower() == 'terminar':
                    #sale del bucle en caso de escribir 'terminar'
                    break
                #verifica que el nombre del alimento sea alfanumerico y no vacio, 'strip' borra espacios en blanco
                if not nombre_alimento.isalnum() or not nombre_alimento.strip():
                    print("Error: El nombre del alimento debe ser alfanumerico y no debe estar vacio.")
                    continue
                
                try:
                    #solicita la nueva cantidad del alimento
                    cantidad = int(input(f"Ingrese la nueva cantidad de '{nombre_alimento}': "))
                    #verifica que la cantidad sea positivia
                    if cantidad < 0:
                        print("Error: La cantidad debe ser un numero entero positivo.")
                        continue
                    #maneja errores si la entrada no es un numero valido
                except ValueError:
                    print("Error: Por favor, ingrese un valor numerico valido para la cantidad.")
                    continue

#agrega el alimento y la nueva cantidad al diccionario de nuevos alimentos
                nuevos_alimentos[nombre_alimento] = cantidad
            
            #modifica el combo con los nuevos datos ingresados
            gestion_combo.modificar_combo(nombre, nuevo_costo, nuevo_margen_ganancia, nuevos_alimentos)


        elif opcion == "4":
            #muestra los combos guardados
            gestion_combo.mostrar_combos()


        elif opcion == "5":
            print("\n Volviendo al Menu Administrativo...")
            break

        else:
            print("\n Opcion no valida, intente de nuevo.")