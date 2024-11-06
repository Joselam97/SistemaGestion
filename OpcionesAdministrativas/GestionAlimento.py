 # Importa la clase que gestiona tipos de alimentosimport shelve
import shelve
from GestionTipoAlimento import GestionTipoAlimento
class GestionAlimento:
    #db_name es la variable que alamacena el nombre del archivo en la base de datos
    def __init__(self, db_name='alimentos.db', tipo_alimento_db_name='tipos_alimentos.db'):
        self.db_name = db_name
        self.tipo_alimento_db_name = tipo_alimento_db_name

#Funcion para incluir alimento
    def incluir_alimento(self, nombre, tipo, costo_compra, margen_ganancia):
        
        with shelve.open(self.tipo_alimento_db_name) as db_tipos:
            
            if nombre.lower() == 'volver':
                print("Operacion cancelada. Volviendo al menú anterior.")
                return
            
            if tipo not in db_tipos:
                print(f"Error: El tipo de alimento '{tipo}' no existe.")
                return
        
        #guarda cada combo en la base de datos 'db_name' con en una variable llamada 'db_alimentos'
        with shelve.open(self.db_name) as db_alimentos:
            
            #Verifica si ya esta incluido en shelve
            if nombre in db_alimentos:
                print(f"Error: Ya existe un alimento con el nombre '{nombre}'.")
                #regresa debido al error
                return
            
            #En caso contrario, se agrega el margen de ganancia que debe estar en un rango de 0 a 100
            if margen_ganancia < 0 or margen_ganancia > 100:
                print("Error: El margen de ganancia debe estar entre 0 y 100.")
                #regresa debido al error
                return
            
            #convierte en fraccion el margen de ganancia y le suma 1, para obtener un 'double' y multiplicarlo al costo de compra
            #Ejemplo: 400 * (1 + 0.2 / 100) = 400 * (1.2) = 480 
            precio_venta = costo_compra * (1 + margen_ganancia / 100)
            #diccionario de la informacion del alimento para guardar en 'db_alimentos'
            db_alimentos[nombre] = {
                'tipo': tipo,
                'costo_compra': costo_compra,
                'margen_ganancia': margen_ganancia,
                'precio_venta': precio_venta
            }
            print(f"Alimento '{nombre}' agregado con éxito.")


#Elimina alimento
    def eliminar_alimento(self, nombre):
        #con shelve se abre el archivo de la base de datos db_alimentos para hacer la consulta
        with shelve.open(self.db_name) as db_alimentos:
            
            #Regresa en caso de no querer eliminar
            if nombre.lower() == 'volver':
                print("Operacion cancelada. Volviendo al menú anterior.")
                return
                
            #En caso de no estar en la base de datos
            if nombre not in db_alimentos:
                print(f"Error: El alimento '{nombre}' no existe.")
                return
            #En caso de estar el alimento asociado a un combo, orden o factura
            if self.alimento_asociado(nombre):
                print(f"Error: No se puede eliminar el alimento '{nombre}' porque está asociado a un combo, orden o factura.")
                return
            #En caso de estar el alimento disponible y no asociado a nada para poder eliminarlo
            del db_alimentos[nombre]
            print(f"Alimento '{nombre}' eliminado con éxito.")


#funcion para modificar el alimento
    def modificar_alimento(self, nombre, nuevo_tipo=None, nuevo_costo_compra=None, nuevo_margen_ganancia=None):
        
        #Regresa en caso de no querer modificar
        if nombre.lower() == 'volver':
            print("Operacion cancelada. Volviendo al menu anterior.")
            return
        #con shelve se abre el archivo de la base de datos db_alimentos para hacer la consulta
        with shelve.open(self.db_name) as db_alimentos:
            
            #En caso no de estar el alimento en la base de datos, mostrara un error
            if nombre not in db_alimentos:
                print(f"Error: El alimento '{nombre}' no existe.")
                return
            alimento = db_alimentos[nombre]
             
            #Modifica el tipo de alimento en caso de no estar vacio
            if nuevo_tipo is not None:
                with shelve.open(self.tipo_alimento_db_name) as db_tipos:
                    
                    #Regresa en caso de no querer modificar
                    if nuevo_tipo.lower() == 'volver':
                        print("Operación cancelada. Volviendo al menú anterior.")
                        return
                    
                    if nuevo_tipo not in db_tipos:
                        print(f"Error: El tipo de alimento '{nuevo_tipo}' no existe.")
                        return
                alimento['tipo'] = nuevo_tipo
            #Mofidica el costo de compra en caso de no estar vacio
            if nuevo_costo_compra is not None:
                alimento['costo_compra'] = nuevo_costo_compra
            #Modifica el margen de ganancia en caso de no estar vacio
            if nuevo_margen_ganancia is not None:
                if nuevo_margen_ganancia < 0 or nuevo_margen_ganancia > 100:
                    print("Error: El margen de ganancia debe estar entre 0 y 100.")
                    return
                alimento['margen_ganancia'] = nuevo_margen_ganancia
            #Modifica como quedaran los nuevos margenes y precios
            alimento['precio_venta'] = alimento['costo_compra'] * (1 + alimento['margen_ganancia'] / 100)
            #Busca el nombre para imprimirlo en pantalla e indicar la modificacion
            db_alimentos[nombre] = alimento
            print(f"Alimento '{nombre}' modificado con éxito.")


#Funcion para mostrar alimentos guardados
    def mostrar_alimentos(self):
        #con shelve se abre el archivo de la base de datos db_alimentos para hacer la consulta
        with shelve.open(self.db_name) as db_alimentos:
            #En caso de no haber nada aun
            if not db_alimentos:
                print("No hay alimentos registrados.")
            #En caso de haber
            else:
                print("\nAlimentos registrados:")
                #Itera por lo datos que tiene guardados
                for nombre, datos in db_alimentos.items():
                    print(f"- {nombre}: Tipo: {datos['tipo']}, Costo de compra: {datos['costo_compra']} colones, "
                          #Imprime cada iteracion de dato guardado por alimento
                          f"Margen de ganancia: {datos['margen_ganancia']}%, Precio de venta: {datos['precio_venta']} colones")



#verificar si el alimento está asociado a un combo, orden o factura
    def alimento_asociado(self, nombre):
        return False 

#funcion para mostrar el menu de alimento
def menu_alimento():
    gestion_alimento = GestionAlimento()
    gestion_tipo_alimento = GestionTipoAlimento()

    while True:
        print("\n--- Menú de Gestión de Alimentos ---")
        print("1. Incluir Alimento")
        print("2. Eliminar Alimento")
        print("3. Modificar Alimento")
        print("4. Mostrar Alimentos")
        print("5. Volver al Menú Administrativo")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            #muestra tipos de alimentos disponibles
            print("\n--- Tipos de Alimentos Disponibles ---")
            gestion_tipo_alimento.mostrar_tipos()
            
            while True:
                tipo = input("Ingrese el tipo de alimento (o 'volver'): ")

                #.lower() sirve para que la entrada sea case-insensitive
                if tipo.lower() == 'volver':
                    print("Operación cancelada. Volviendo al menu de gestión de alimentos.")
                    break
                
                if gestion_tipo_alimento.existe_tipo(tipo):
                    break  #sale del bucle si el tipo es valido
                else:
                    print(f"Advertencia: El tipo de alimento '{tipo}' no existe en la lista de tipos de alimentos. Intente de nuevo.")

            #si se cancela la operacion, continuar al siguiente ciclo
            if tipo.lower() == 'volver':
                continue
            
            nombre = input("Ingrese el nombre del alimento: ")
            
            #valida el costo de compra
            while True:
                try:
                    costo_compra = float(input("Ingrese el costo de compra: "))
                    break  #sale del bucle
                except ValueError: #maneja el error para que se ingrese un numero
                    print("El costo de compra debe ser un número. Inténtalo de nuevo.")

            #valida para margen de ganancia
            while True:
                try:
                    margen_ganancia = float(input("Ingrese el margen de ganancia (en %): "))
                    break  #sale del bucle
                except ValueError: #maneja el error
                    print("El margen de ganancia debe ser un número. Inténtalo de nuevo.")
            gestion_alimento.incluir_alimento(nombre, tipo, costo_compra, margen_ganancia)

        #opcion para eliminar alimentos, los muestra antes de elegir
        elif opcion == "2":
            gestion_alimento.mostrar_alimentos()
            print("\n --- Alimentos a eliminar --- \n")
            nombre = input("Ingrese el nombre del alimento a eliminar (o 'volver'): ")
            gestion_alimento.eliminar_alimento(nombre)

        #opcion para modificar alimentos, los muestra antes de elegir
        elif opcion == "3":
            gestion_alimento.mostrar_alimentos()
            print("\n --- Alimentos a modificar --- \n")
            nombre = input("Ingrese el nombre del alimento a modificar (o 'volver'): ")
            if nombre.lower() == 'volver':
                print("Operación cancelada. Volviendo al menú de gestión de alimentos.")
                continue
            
            nuevo_tipo = input("Ingrese el nuevo tipo de alimento (deje en blanco si no desea cambiar): ")
            nuevo_tipo = nuevo_tipo if nuevo_tipo else None
            nuevo_costo_compra = input("Ingrese el nuevo costo de compra (deje en blanco si no desea cambiar): ")
            nuevo_costo_compra = float(nuevo_costo_compra) if nuevo_costo_compra else None
            nuevo_margen_ganancia = input("Ingrese el nuevo margen de ganancia (en %, deje en blanco si no desea cambiar): ")
            nuevo_margen_ganancia = float(nuevo_margen_ganancia) if nuevo_margen_ganancia else None
            gestion_alimento.modificar_alimento(nombre, nuevo_tipo, nuevo_costo_compra, nuevo_margen_ganancia)

        elif opcion == "4":
            gestion_alimento.mostrar_alimentos()
            

        elif opcion == "5":
            print("Volviendo al Menú Administrativo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Iniciar el menú
if __name__ == "__main__":
    menu_alimento()
