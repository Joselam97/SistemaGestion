import shelve
from datetime import datetime
from GestionOrdenes import GestionOrdenes
from GestionCombos import GestionCombo
from GestionAlimento import GestionAlimento
from CrearUsuario import CrearUsuario

class Facturacion:
    def __init__(self):
        #inicializa las instancias de otras clases para poder usar sus atributos
        self.gestion_ordenes = GestionOrdenes()
        self.gestion_combos = GestionCombo()
        self.gestion_alimentos = GestionAlimento()
        self.crear_usuario = CrearUsuario()
        
        #define los nombres de las bases de datos en el sistema
        self.facturas_db_name = 'facturas.db'
        self.redenciones_db_name = 'redenciones.db'
        self.puntos_db_name = 'puntos.db'

    def generar_identificador_factura(self):
        #genera un identificador unico de factura usando la fecha y hora actual
        return f"FACT-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}"

    def obtener_puntos_usuario(self, usuario):
        #abre la base de datos de puntos y obtiene los puntos del usuario, retorna 0 si no existe
        with shelve.open(self.puntos_db_name) as db_puntos:
            return db_puntos.get(usuario, 0)

    def actualizar_puntos_usuario(self, usuario, puntos):
        #actualiza los puntos de un usuario, sumandolos a los puntos actuales
        with shelve.open(self.puntos_db_name, writeback=True) as db_puntos:
            db_puntos[usuario] = db_puntos.get(usuario, 0) + puntos

    def registrar_redencion(self, usuario, id_factura, puntos_redimidos):
        #registra una redencion de puntos en la base de datos de redenciones, almacenando detalles
        with shelve.open(self.redenciones_db_name, writeback=True) as db_redenciones:
            #guarda todo en un diccionario
            db_redenciones[id_factura] = {
                "fecha": datetime.now(),
                "usuario": usuario,
                "puntos_redimidos": puntos_redimidos
            }

    def facturar(self, usuario, id_orden):
        #factura una orden especifica, verificando que exista y que no haya sido ya facturada
        with shelve.open(self.gestion_ordenes.ordenes_db_name, writeback=True) as db_ordenes, shelve.open(self.facturas_db_name, writeback=True) as db_facturas:
            if usuario not in db_ordenes or id_orden not in db_ordenes[usuario] or db_ordenes[usuario][id_orden]["facturada"]:
                print("La orden no existe o ya ha sido facturada.")
                return

#recupera los datos de la orden y genera un nuevo identificador de factura
            orden = db_ordenes[usuario][id_orden]
            id_factura = self.generar_identificador_factura()
            fecha_hora = datetime.now()

            subtotal = 0
            impuesto_alimentos = 0
            impuesto_combos = 0

            #calcula todos los margenes relacionados a alimentos individuales contenidos en la orden
            print("\nAlimentos:")
            for nombre, cantidad in orden['alimentos'].items():
                item_info = self.gestion_alimentos.obtener_info_alimento(nombre)
                if item_info and 'precio_venta' in item_info:
                    precio = item_info['precio_venta']
                    precio_linea = precio * cantidad
                    subtotal += precio_linea
                    impuesto_alimento = precio_linea * 0.05 #impuesto del 5% en alimentos individuales
                    impuesto_alimentos += impuesto_alimento
                    print(f" - {nombre}: {cantidad} x {precio} = {precio_linea} (Impuesto: {impuesto_alimento})")
                else:
                    print(f" - {nombre}: formato invalido o falta de información, no se puede procesar")

            #calcula todos los margenes relacionados a combos contenidos en la orden
            print("\nCombos:")
            for nombre, cantidad in orden['combos'].items():
                combo_info = self.gestion_combos.obtener_info_combo(nombre)
                if combo_info and 'precio_venta' in combo_info:
                    precio = combo_info['precio_venta']
                    precio_linea = precio * cantidad
                    subtotal += precio_linea
                    impuesto_combo = precio_linea * 0.13 #impuesto del 13% en combos
                    impuesto_combos += impuesto_combo
                    print(f" - {nombre}: {cantidad} x {precio} = {precio_linea} (Impuesto: {impuesto_combo})")
                else:
                    print(f" - {nombre}: formato invalido o falta de informacion, no se puede procesar")

#calcula el total de impuesto y el monto final
            total_impuesto = impuesto_alimentos + impuesto_combos
            total = subtotal + total_impuesto
            puntos_disponibles = self.obtener_puntos_usuario(usuario)
            descuento = 0

            #pregunta para redimir puntos y aplicar descuento
            try:
                redimir_puntos = input("¿Desea redimir puntos? (s/n): ").strip().lower() == 's'
            except ValueError:
                print("Entrada invalida. Intente nuevamente.")
                return

#si se redimen puntos, calcula el descuento en la factura y los puntos redimidos
            if redimir_puntos and puntos_disponibles > 0:
                while True:
                    try:
                        puntos_redimir = int(input(f"Tienes {puntos_disponibles} puntos disponibles. Ingrese la cantidad de puntos a redimir: "))
                        if puntos_redimir > puntos_disponibles or puntos_redimir * 4.75 > total:
                            puntos_redimir = min(puntos_disponibles, int(total / 4.75))
                        descuento = puntos_redimir * 4.75
                        total -= descuento
                        self.registrar_redencion(usuario, id_factura, puntos_redimir)
                        self.actualizar_puntos_usuario(usuario, -puntos_redimir)
                        break
                    except ValueError:
                        print("Error: Ingrese un numero entero para los puntos.")

#calcula los puntos ganados en esta transaccion y los actualiza en la cuenta del usuario
            puntos_ganados = int(total / 1000)
            self.actualizar_puntos_usuario(usuario, puntos_ganados)

            #almacena la factura en la base de datos de facturas y marca la orden como facturada
            db_facturas[id_factura] = {
                "usuario": usuario,
                "id_orden": id_orden,
                "fecha_hora": fecha_hora,
                "subtotal": subtotal,
                "total_impuesto": total_impuesto,
                "descuento": descuento,
                "total": total,
                "puntos_ganados": puntos_ganados
            }
            orden["facturada"] = True

            #muestra el comprobante al usuario
            print("\n--- Comprobante de Factura ---")
            print(f"ID Factura: {id_factura}")
            print(f"Fecha y Hora: {fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Impuesto Alimentos (5%): {impuesto_alimentos:.2f}")
            print(f"Impuesto Combos (13%): {impuesto_combos:.2f}")
            print(f"Total Impuesto: {total_impuesto:.2f}")
            print(f"Descuento: {descuento:.2f}")
            print(f"Total a Pagar: {total:.2f}")
            print(f"Puntos Ganados: {puntos_ganados}")
            print("\n--- Fin del Comprobante ---")

    def mostrar_facturas_usuario(self, usuario):
        #muestra todas las facturas de un usuario especifico, devolviendo sus identificadores
        facturas_ids = []
        with shelve.open(self.facturas_db_name) as db_facturas:
            print(f"\n--- Facturas del usuario '{usuario}' ---")
            for id_factura, datos in db_facturas.items():
                if datos["usuario"] == usuario:
                    print(f"ID Factura: {id_factura}, Fecha y Hora: {datos['fecha_hora']}")
                    facturas_ids.append(id_factura)

            if not facturas_ids:
                print("No se encontraron facturas para este usuario.")
        return facturas_ids

    def consultar_factura(self, id_factura):
        #muestra los detalles de una factura especifica
        with shelve.open(self.facturas_db_name) as db_facturas:
            if id_factura in db_facturas:
                factura = db_facturas[id_factura]
                print(f"ID Factura: {id_factura}\nUsuario: {factura['usuario']}\nID Orden: {factura['id_orden']}")
                print(f"Fecha y Hora: {factura['fecha_hora']}\nSubtotal: {factura['subtotal']}\nImpuesto: {factura['total_impuesto']}")
                print(f"Descuento: {factura['descuento']}\nTotal: {factura['total']}")
            else:
                print("Factura no encontrada.")

    def reporte_ventas(self, fecha_inicio, fecha_fin):
        #genera un resumen de ventas para un rango de fechas especifico
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        cantidad_facturas = total_facturado = subtotal_facturado = impuesto_recaudado = 0
        vendedores = {}
    
        #abre la base de datos de facturas para iterar sobre ellas
        with shelve.open(self.facturas_db_name) as db_facturas:
            for id_factura, factura in db_facturas.items():
                factura_fecha = factura['fecha_hora']
                if isinstance(factura_fecha, str):
                    factura_fecha = datetime.strptime(factura_fecha, '%Y-%m-%d %H:%M:%S')

                #verifica si la fecha de la factura está dentro del rango especificado
                if fecha_inicio <= factura_fecha <= fecha_fin:
                    cantidad_facturas += 1
                    subtotal_facturado += factura['subtotal']
                    impuesto_recaudado += factura['total_impuesto']
                    total_facturado += factura['total']  #suma el total después del impuesto
                    usuario = factura['usuario']
                    #cuenta la cantidad de facturas por cada vendedor (usuario)
                    vendedores[usuario] = vendedores.get(usuario, 0) + 1

        #corrige el calculo de la ganancia para evitar negativos
        ganancia = subtotal_facturado  #considera que la ganancia real es el subtotal facturado
        print(f"\n--- Resumen de Ventas ---")
        print(f"Cantidad de facturas en rango: {cantidad_facturas}")
        print(f"Total facturado: {total_facturado}")
        print(f"Subtotal facturado: {subtotal_facturado}")
        print(f"Ganancia: {ganancia}")
        print(f"Impuesto recaudado: {impuesto_recaudado}")
        print("\nLista de vendedores y cantidad de facturas generadas:")
    
    #itera sobre las facturas que tiene cada usuario (vendedor)
        for vendedor, facturas in vendedores.items():
            print(f"Usuario '{vendedor}': {facturas} facturas")

    def menu_facturacion(self):
        while True:
            print("\n--- Menu de Gestión de Facturacion ---")
            print("1. Facturar Orden")
            print("2. Consultar Factura")
            print("3. Generar Reporte de Ventas")
            print("4. Volver al Menu Administrativo")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                usuario = input("\nIngrese su nombre de usuario: ")
                if self.crear_usuario.verificar_usuario(usuario):
                    #obtiene las facturas del usurio
                    ordenes = self.gestion_ordenes.mostrar_ordenes_usuario(usuario, facturadas=False)
                    if ordenes:
                        id_orden = input("Ingrese el identificador de la orden a facturar: ")
                        if id_orden in ordenes:
                            self.facturar(usuario, id_orden)
                        else:
                            print("Orden no valida seleccionada.")

            elif opcion == "2":
                usuario = input("\nIngrese su nombre de usuario: ")
                if self.crear_usuario.verificar_usuario(usuario):
                    #muestra las facturas existen del usuario
                    facturas = self.mostrar_facturas_usuario(usuario)
                    if facturas:
                        id_factura = input("\nIngrese el identificador de la factura a consultar: ")
                        if id_factura in facturas:
                            self.consultar_factura(id_factura)
                        else:
                            print("Factura no valida seleccionada.")

            elif opcion == "3":
                try:
                    fecha_inicio = input("\nIngrese la fecha de inicio (YYYY-MM-DD): ")
                    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
                    self.reporte_ventas(fecha_inicio, fecha_fin)
                except ValueError:
                    print("Fecha no valida. Intente de nuevo en el formato YYYY-MM-DD.")

            elif opcion == "4":
                print("\n Volviendo al Menu Administrativo...")
                break

            else:
                print("\n Opcion no valida. Intente de nuevo.")