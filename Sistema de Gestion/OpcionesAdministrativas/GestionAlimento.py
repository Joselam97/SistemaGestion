import shelve
from GestionTipoAlimento import GestionTipoAlimento  # Importar la clase que gestiona tipos de alimentos

class GestionAlimento:
    def __init__(self, db_name='alimentos.db', tipos_db_name='tipos_alimentos.db'):
        # Usamos shelve para almacenar los alimentos y los tipos de alimentos
        self.db_name = db_name
        self.tipos_db_name = tipos_db_name
        self.gestion_tipo_alimento = GestionTipoAlimento(tipos_db_name)

    def incluir_alimento(self, nombre, tipo_indice, costo_compra, margen_ganancia):
        with shelve.open(self.db_name) as db_alimentos, shelve.open(self.tipos_db_name) as db_tipos:
            # Verificar si el alimento ya existe por nombre
            if nombre in db_alimentos:
                print(f"Error: Ya existe un alimento con el nombre '{nombre}'.")
                return

            # Verificar si el tipo de alimento existe por índice
            tipos_list = list(db_tipos.keys())
            if tipo_indice < 0 or tipo_indice >= len(tipos_list):
                print("Error: El índice de tipo de alimento es inválido.")
                return
            tipo_seleccionado = tipos_list[tipo_indice]

            # Calcular el precio de venta según el margen de ganancia
            if margen_ganancia < 0 or margen_ganancia > 100:
                print("Error: El margen de ganancia debe estar entre 0 y 100.")
                return
            precio_venta = costo_compra * (1 + margen_ganancia / 100)

            # Almacenar el nuevo alimento
            db_alimentos[nombre] = {
                'tipo': tipo_seleccionado,
                'costo_compra': costo_compra,
                'margen_ganancia': margen_ganancia,
                'precio_venta': precio_venta
            }
            print(f"Alimento '{nombre}' agregado con éxito.")

    def eliminar_alimento(self, nombre):
        with shelve.open(self.db_name) as db_alimentos:
            # Verificar si el alimento existe
            if nombre not in db_alimentos:
                print(f"Error: El alimento '{nombre}' no existe.")
                return

            # Verificar si el alimento está asociado a algún combo, orden o factura (simulado)
            if self.alimento_asociado(nombre):
                print(f"Error: No se puede eliminar el alimento '{nombre}' porque está asociado a un combo, orden o factura.")
                return

            # Eliminar el alimento
            del db_alimentos[nombre]
            print(f"Alimento '{nombre}' eliminado con éxito.")

    def modificar_alimento(self, nombre, nuevo_tipo_indice=None, nuevo_costo_compra=None, nuevo_margen_ganancia=None):
        with shelve.open(self.db_name) as db_alimentos, shelve.open(self.tipos_db_name) as db_tipos:
            # Verificar si el alimento existe
            if nombre not in db_alimentos:
                print(f"Error: El alimento '{nombre}' no existe.")
                return

            # Modificar los valores si se proporcionan nuevos
            alimento = db_alimentos[nombre]

            # Cambiar tipo de alimento si se pasa un nuevo índice
            if nuevo_tipo_indice is not None:
                tipos_list = list(db_tipos.keys())
                if nuevo_tipo_indice < 0 or nuevo_tipo_indice >= len(tipos_list):
                    print("Error: El índice de tipo de alimento es inválido.")
                    return
                alimento['tipo'] = tipos_list[nuevo_tipo_indice]

            # Cambiar el costo de compra si se proporciona uno nuevo
            if nuevo_costo_compra is not None:
                alimento['costo_compra'] = nuevo_costo_compra

            # Cambiar el margen de ganancia si se proporciona uno nuevo
            if nuevo_margen_ganancia is not None:
                if nuevo_margen_ganancia < 0 or nuevo_margen_ganancia > 100:
                    print("Error: El margen de ganancia debe estar entre 0 y 100.")
                    return
                alimento['margen_ganancia'] = nuevo_margen_ganancia

            # Recalcular el precio de venta
            alimento['precio_venta'] = alimento['costo_compra'] * (1 + alimento['margen_ganancia'] / 100)

            # Guardar los cambios
            db_alimentos[nombre] = alimento
            print(f"Alimento '{nombre}' modificado con éxito.")

    def mostrar_alimentos(self):
        with shelve.open(self.db_name) as db_alimentos:
            if not db_alimentos:
                print("No hay alimentos registrados.")
            else:
                print("\nAlimentos registrados:")
                for nombre, datos in db_alimentos.items():
                    print(f"- {nombre}: Tipo: {datos['tipo']}, Costo de compra: {datos['costo_compra']} colones, "
                          f"Margen de ganancia: {datos['margen_ganancia']}%, Precio de venta: {datos['precio_venta']} colones")

    def alimento_asociado(self, nombre):
        # Simular que no hay alimentos asociados para este ejemplo
        # En un proyecto real, deberías verificar si este alimento está asociado a un combo, orden o factura
        return False

# Ejemplo de uso del sistema
gestion_alimento = GestionAlimento()

# Suponiendo que ya tienes algunos tipos de alimentos en 'tipos_alimentos.db'
gestion_alimento.mostrar_alimentos()

# Incluir nuevos alimentos (se asume que los tipos de alimentos ya están creados)
gestion_alimento.incluir_alimento("Manzana", 0, 100, 20)
gestion_alimento.incluir_alimento("Pan", 1, 50, 30)

# Modificar un alimento
gestion_alimento.modificar_alimento("Manzana", nuevo_margen_ganancia=25)

# Mostrar todos los alimentos
gestion_alimento.mostrar_alimentos()

# Eliminar un alimento
gestion_alimento.eliminar_alimento("Pan")

# Mostrar nuevamente los alimentos
gestion_alimento.mostrar_alimentos()
